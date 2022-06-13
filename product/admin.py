from django.contrib import admin

from product.models import Category, Product, Product_Image


@admin.register(Product)
class Product_Admin(admin.ModelAdmin):
    list_display = ['title', 'price', 'category', 'created_time']
    search_fields = ['title']


@admin.register(Category)
class Category_Admin(admin.ModelAdmin):
    list_display = ['title', 'parent','level', 'created_time']
    search_fields = ['title']


@admin.register(Product_Image)
class Product_Image_Admin(admin.ModelAdmin):
    list_display = ['product', 'sort', 'image', 'created_time']
    search_fields = ['product__title']
