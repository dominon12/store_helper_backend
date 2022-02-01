from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.authentication import TokenAuthentication

from . import serializers


class UserDetail(APIView):
    authentication_classes = [TokenAuthentication]

    def get(self, request):
        user = request.user
        serializer = serializers.UserSerializer(instance=user)
        return Response(serializer.data)