from django.shortcuts import render
from django.views.generic import View

from rest_framework.views import Response
from rest_framework.views import APIView

from .models import Item
from .serializers import *


class ItemApiView(APIView):
    def get(self, request, *args, **kwargs):
        items = Item.objects.filter(published=True)
        serializer = ItemSerializer(items, many=True)
        return Response(serializer.data)


class PurchaseApiView(APIView):
    def post(self, request):
        pass