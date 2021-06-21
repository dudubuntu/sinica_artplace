from django.shortcuts import render
from django.views.generic import View
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.views import Response

from .models import ContactUs
from .forms import ContactUsForm


class ContactUsView(APIView):
    def post(self, request, *args, **kwargs):
        form = ContactUsForm(data=request.POST)
        if form.is_valid():
            form.save()
            return Response(data={"message": "Ваш запрос принят. Ожидайте звонка"}, status=status.HTTP_201_CREATED)
        else:
            return Response(data={"error": form.errors}, status=status.HTTP_400_BAD_REQUEST)