from django.urls import path
from rest_framework.authtoken.views import ObtainAuthToken

from . import views

app_name = 'auth'

urlpatterns = [
    path('token/', ObtainAuthToken.as_view(), name='auth'),
    path('current/', views.UserDetail.as_view(), name='current-account'),
]