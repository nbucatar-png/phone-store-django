from django.contrib import admin
from django.db import models

from .models import Order, OrderItem, Product


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('brand', 'name', 'category', 'price', 'stock', 'featured')
    list_filter = ('category', 'featured')
    search_fields = ('brand', 'name')


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'full_name', 'phone', 'status', 'created_at', 'total')
    list_filter = ('status', 'created_at')
    search_fields = ('full_name', 'phone', 'address')


@admin.register(OrderItem)
class OrderItemAdmin(admin.ModelAdmin):
    list_display = ('order', 'product', 'quantity', 'price', 'total')
