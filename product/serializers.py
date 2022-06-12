from rest_framework import serializers

from product.models import Category, Product, Product_Image


class Product_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'


class Category_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class Product_Image_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Product_Image
        fields = '__all__'
