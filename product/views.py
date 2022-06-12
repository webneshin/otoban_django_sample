from django.shortcuts import render
from rest_framework import permissions, viewsets

from product.models import Category, Product, Product_Image
from product.serializers import Category_Serializer, Product_Serializer, Product_Image_Serializer


class Product_ViewSet(viewsets.ModelViewSet):
    """
    Products
    """
    queryset = Product.objects.all()
    serializer_class = Product_Serializer
    # permission_classes = [permissions.DjangoModelPermissionsOrAnonReadOnly]
    filterset_fields = {
        'title': ['exact', ],
        'category': ['exact', ],
    }
    search_fields = ['title', 'category', 'price', ]


class Category_ViewSet(viewsets.ModelViewSet):
    """
    Categories
    """
    queryset = Category.objects.all()
    serializer_class = Category_Serializer
    # permission_classes = [permissions.DjangoModelPermissionsOrAnonReadOnly]
    filterset_fields = {
        'title': ['exact', ],
        'parent': ['exact', ],
    }
    search_fields = ['title', 'description']


class Product_Image_ViewSet(viewsets.ModelViewSet):
    """
    Product Images
    """
    queryset = Product_Image.objects.all()
    serializer_class = Product_Image_Serializer
    # permission_classes = [permissions.DjangoModelPermissionsOrAnonReadOnly]
    filterset_fields = {
        'product': ['exact', ],
    }
    search_fields = ['product', ]
