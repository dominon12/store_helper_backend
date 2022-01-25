from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.authentication import TokenAuthentication

from . import models, serializers


class ProductViewSet(ModelViewSet):
    queryset = models.Product.objects.all()
    serializer_class = serializers.ProductSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    authentication_classes = [TokenAuthentication]