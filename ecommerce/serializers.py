from rest_framework.serializers import ModelSerializer
from .models import Product, Category

class CategorySerializer(ModelSerializer):

    class Meta:
        model = Category
        fields = ["id", "name"]

class ProductSerializer(ModelSerializer):

    categories = CategorySerializer(many=True, read_only=False)

    class Meta:
        model = Product
        fields = ['id', 'name', 'description', 'price', 'categories', 'image', 'stock']

class ManageProductSerializer(ModelSerializer):

    class Meta:
        model = Product
        fields = ['name', 'description', 'price', 'categories', 'image', 'stock']

class ProductApiSerializer(ModelSerializer):

    class Meta:
        model = Product
        fields = ['name', 'description', 'price', 'categories', 'image', 'stock']