from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from .models import Product, Category

class CategorySerializer(ModelSerializer):

    class Meta:
        model = Category
        fields = ["id", "name"]

class ProductSerializer(ModelSerializer):

    categories = CategorySerializer(many=True, read_only=True)

    class Meta:
        model = Product
        fields = ['id', 'name', 'description', 'price', 'categories', 'image']

class ManageProductSerializer(ModelSerializer):

    class Meta:
        model = Product
        fields = ['name', 'description', 'price', 'categories', 'image']

class ProductApiSerializer(ModelSerializer):

    class Meta:
        model = Product
        fields = ['name', 'description', 'price', 'image']