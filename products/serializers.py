from rest_framework import serializers

from store_helper_backend.service import build_absolute_uri
from . import models 



class ProductSerializer(serializers.ModelSerializer):
    image = serializers.SerializerMethodField()

    class Meta:
        model = models.Product
        fields = ('pk', 'name', 'description', 'price', 'image')

    def get_image(self, obj):
        return build_absolute_uri(
            request=self.context.get('request'),
            relative_url=obj.image.url
        )
