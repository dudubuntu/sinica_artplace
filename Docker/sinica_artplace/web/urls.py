from django.urls import path, include

from .views import *


app_name = 'web'
urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('contact_us/', include('contactus.urls')),
]