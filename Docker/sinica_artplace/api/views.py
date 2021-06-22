from django.shortcuts import render
from django.views.generic import View
from django.http import request

from rest_framework.views import Response
from rest_framework.views import APIView
from rest_framework.generics import ListAPIView

from .models import Item
from .serializers import *


class ItemApiView(APIView):
    def get(self, request: request.HttpRequest, *args, **kwargs):
        if 'articul_list' in request.GET:                           #переписать без параметров get запроса
            items = Item.objects.filter(published=True, articul__in=request.GET['articul_list'])
        else:
            items = Item.objects.filter(published=True)
        serializer = ItemSerializer(items, many=True)
        return Response(serializer.data)


class PurchaseApiView(APIView):
    def post(self, request):
        pass


class ReviewApiView(ListAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer