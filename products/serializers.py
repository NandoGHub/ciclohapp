from rest_framework import serializers
from .models import Product


class ProductSerializer(serializers.ModelSerializer):

    class Meta:
        model = Product
        fields = ('uuid', 'name', 'price', 'stock')
        extra_kwargs = {
            'id': {'allow_null': False, 'required': False},
            'uuid': {'allow_null': False, 'required': True},
            'name': {'allow_null': False, 'required': True},
            'price': {'allow_null': False, 'required': True},
            'stock': {'allow_null': False, 'required': True}
        }
