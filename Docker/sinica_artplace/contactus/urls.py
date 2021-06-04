from django.urls import path

from .views import ContactUsView


app_name = 'contactus'
urlpatterns = [
    path('leave_request/', ContactUsView.as_view(), name='leave_request'),
]