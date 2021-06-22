from django.urls import path, include

from .views import *


app_name = 'api'
urlpatterns = [
    path('item_list/', ItemApiView.as_view(), name='item_list'),

    path('review_list/', ReviewApiView.as_view(), name='review_list'),

    path('cart/', include('cart.urls')),
]