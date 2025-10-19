from decimal import Decimal
from rest_framework import serializers
from .models import Product, Collection

class CollectionSerializer(serializers.ModelSerializer):
  class Meta:
    model = Collection
    fields = [
      'id',
      'title',
      'products_count'
    ]
  products_count = serializers.IntegerField()

class ProductSerializer(serializers.ModelSerializer):
  class Meta:
    model = Product
    # try not to use __all__, because it may expose sensitive data and leaks implementation details
    fields = [
      'id',
      'title',
      'description',
      'slug',
      'inventory',
      'unit_price',
      'price_with_tax',
      'collection'
    ]
 
  price_with_tax = serializers.SerializerMethodField(method_name='calulate_price_with_tax')
  # collection = serializers.HyperlinkedRelatedField(
  #   queryset=Collection.objects.all(),
  #   view_name='collection-detail'
  # )

  def calulate_price_with_tax(self, product: Product):
    return product.unit_price * Decimal(1.1)