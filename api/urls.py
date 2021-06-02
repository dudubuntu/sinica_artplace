from django.urls import path, include

from .views import *


app_name = 'api'
urlpatterns = [
    path('item_list', ItemApiView.as_view(), name='item_list'),

]