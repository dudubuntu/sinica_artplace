from django.shortcuts import render
from django.views.generic import View
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.views import Response

from .models import ContactUs
from .forms import ContactUsForm
from .serializers import ContactUsSerializer


class ContactUsView(APIView):
    def post(self, request, *args, **kwargs):
        serializer = ContactUsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data={"message": "Ваш запрос принят. Ожидайте звонка"}, status=status.HTTP_201_CREATED)
        else:
            return Response(data={"error": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)