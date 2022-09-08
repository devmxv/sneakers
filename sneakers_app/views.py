from django.shortcuts import render
from .models import Brand, Sneaker
from .serializer import BrandSerializer, SneakerSerializer
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import api_view

# Create your views here.
@api_view(['GET'])
def get_sneakers(request):
  sneakers = Sneaker.objects.all()
  serializer = SneakerSerializer(sneakers, many=True)
  return Response(serializer.data)


@api_view(['GET'])
def get_brands(request):
  brands = Brand.objects.all()
  serializer = BrandSerializer(brands, many=True)
  return Response(serializer.data)

@api_view(['GET'])
def get_brand(request, id):
  brand = Brand.objects.get(id=id)
  serializer = BrandSerializer(brand)
  return Response(serializer.data)
