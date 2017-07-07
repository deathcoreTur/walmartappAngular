from rest_framework import serializers
from .models import Product

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['upc', 'main_image', 'name', 'brand', 'model_product', 'quantity', 'in_stock',
                  'price', 'free_shipping', 'updated']