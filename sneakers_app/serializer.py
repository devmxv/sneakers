from rest_framework import serializers
from sneakers_app.models import Brand, Sneaker


class BrandSerializer(serializers.ModelSerializer):
  class Meta:
    model = Brand
    fields = '__all__'

class SneakerSerializer(serializers.ModelSerializer):
  class Meta:
    model = Sneaker
    fields = '__all__'
