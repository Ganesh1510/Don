from django.urls import path
from .views import  send_email_api

urlpatterns = [
    path('send_email_api/',send_email_api, name='send_email_api'),
]