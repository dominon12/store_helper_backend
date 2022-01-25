from django.urls import path
from rest_framework.authtoken.views import ObtainAuthToken


app_name = 'auth'

urlpatterns = [
    path('token/', ObtainAuthToken.as_view(), name='auth'),
]