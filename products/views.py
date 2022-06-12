from math import prod
from os import stat
from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import ProductSerializer
from .models import Product

class ProductView(APIView):
    def get(self, request, product_id):
        queryset = Product.objects.filter(id=product_id).first()

        if queryset:
            serializer = ProductSerializer(queryset)
        else:
            queryset = Product.objects.all()
            serializer = ProductSerializer(queryset, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, product_id):
        serializer = ProductSerializer(data=request.data)

        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        Product.objects.create(**request.data)

        queryset = Product.objects.all()
        serializer = ProductSerializer(queryset, many=True)

        return Response(serializer.data, status=status.HTTP_201_CREATED)


    def put(self, request, product_id):
        product = get_object_or_404(Product, id=product_id)

        serializer = ProductSerializer(data=request.data)

        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        product.name = request.data['name']
        product.code = request.data['code']
        product.category = request.data['category']
        product.provider = request.data['provider']
        product.amount = request.data['amount']

        product.save()

        queryset = Product.objects.all()
        serializer = ProductSerializer(queryset, many=True)

        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def delete(self, request, product_id):
        product = get_object_or_404(Product, id=product_id)

        product.delete()

        queryset = Product.objects.all()
        serializer = ProductSerializer(queryset, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)