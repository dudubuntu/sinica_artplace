from django.http import HttpRequest
from rest_framework.views import APIView, Response
from rest_framework import status
from rest_framework.request import Request

from .objects import Cart, CartException
from api.models import Item


class CartApiView(APIView):
    def get(self, request, *args, **kwargs):
        """get cart json formatted"""
        cart = Cart(request, Item)
        return Response(data=cart.get_json_cart())

    def post(self, request: HttpRequest, *args, **kwargs):
        """add item to cart
        {"articul": "1000", extra: {"quantity": "100", "price": "10000"}}
        """
        cart = Cart(request, Item)

        try:
            articul, extra = request.data['articul'], request.data['extra']
            cart.add(articul, price=extra['price'], quantity=extra['quantity'])
        except CartException as exc:
            return Response(data={"error": f'CartException: {str(exc)}'}, status=status.HTTP_400_BAD_REQUEST)
        except KeyError as exc:
            return Response(data={"error": f'{str(exc)}'}, status=status.HTTP_400_BAD_REQUEST)

        return Response(data=cart.get_json_cart(), status=status.HTTP_200_OK)

    def put(self, request, *args, **kwargs):
        """delete item from cart
        {"articul": "1000", "quantity": "100"}
        """
        cart = Cart(request, Item)
        articul, quantity = request.data.values()
        try:
            cart.delete(articul, quantity)
        except CartException as exc:
            return Response(data={"error": f'CartException: {str(exc)}'}, status=status.HTTP_400_BAD_REQUEST)
        return Response(data=cart.get_json_cart(), status=status.HTTP_200_OK)

    def delete(self, request, *args, **kwargs):
        """clear cart"""
        cart = Cart(request, Item)
        cart.clear()
        return Response(data=cart.get_json_cart(), status=status.HTTP_200_OK)