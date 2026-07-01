from django.contrib import admin
from .models import Product, Category, CartItem, CollectionItem

# Register your models here.

class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'price')
    search_fields = ('id', 'name', 'price')
    list_filter = ('name', 'price')
    ordering = ['id', 'name']

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    search_fields = ('id', 'name')
    list_filter = ('id', 'name')
    ordering = ['id', 'name']

class CartItemAdmin(admin.ModelAdmin):
    list_display = ('id', 'quantity')
    search_fields = ('id', 'quantity')
    list_filter = ('id', 'quantity')
    ordering = ['id', 'quantity']

class CollectionItemAdmin(admin.ModelAdmin):
    list_display = ('id', 'quantity')
    search_fields = ('id', 'quantity')
    list_filter = ('id', 'quantity')
    ordering = ['id', 'quantity']

admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(CollectionItem, CollectionItemAdmin)
admin.site.register(CartItem, CartItemAdmin)