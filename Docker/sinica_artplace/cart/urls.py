from django.urls import path

from .views import *


app_name = 'cart'
urlpatterns = [
    path('get_cart/', CartApiView.as_view(), name='get_cart'),
    path('add_item/', CartApiView.as_view(), name='add_item'),
    path('delete_item/', CartApiView.as_view(), name='delete_item'),
    path('clear_cart/', CartApiView.as_view(), name='clear_cart'),
]