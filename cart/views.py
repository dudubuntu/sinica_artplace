from django.http import HttpRequest
from rest_framework.views import APIView, Response
from rest_framework import status
from rest_framework.request import Request

from .objects import Cart
from api.models import Item


class CartApiView(APIView):
    def get(self, request, *args, **kwargs):
        """get cart json formatted"""
        cart = Cart(request, Item)
        return Response(data=cart.get_json_cart())

    def post(self, request: HttpRequest, *args, **kwargs):
        """add item to cart"""
        cart = Cart(request, Item)
        articul, quantity = request.data.popitem()
        cart.add(articul, quantity)
        return Response(data=cart.get_json_cart(), status=status.HTTP_200_OK)

    def put(self, request, *args, **kwargs):
        """delete item from cart"""
        cart = Cart(request, Item)
        articul, quantity = request.data.popitem()
        cart.delete(articul, quantity)
        return Response(data=cart.get_json_cart(), status=status.HTTP_200_OK)

    def delete(self, request, *args, **kwargs):
        """clear cart"""
        cart = Cart(request, Item)
        cart.clear()
        return Response(data=cart.get_json_cart(), status=status.HTTP_200_OK)