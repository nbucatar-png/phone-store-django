from django.contrib import admin
from django.db import models


class Product(models.Model):
    CATEGORY_CHOICES = [('phone', 'Phone'), ('accessory', 'Accessory')]
    category = models.CharField('Category', max_length=20, choices=CATEGORY_CHOICES, default='phone')
    brand = models.CharField('Brand', max_length=100)
    name = models.CharField('Name', max_length=200)
    description = models.TextField('Description')
    price = models.DecimalField('Price', max_digits=10, decimal_places=2)
    image_url = models.URLField('Image URL', max_length=500, blank=True)
    stock = models.PositiveIntegerField('In stock', default=1)
    featured = models.BooleanField('Featured on home page', default=False)
    created_at = models.DateTimeField('Created', auto_now_add=True)

    class Meta:
        verbose_name = 'Product'
        verbose_name_plural = 'Products'
        ordering = ['-created_at']

    def __str__(self):
        return f'{self.brand} {self.name}'


class Order(models.Model):
    STATUS_CHOICES = [('pending', 'Pending'), ('processed', 'Processing'), ('completed', 'Completed')]
    full_name = models.CharField('Full name', max_length=200)
    phone = models.CharField('Phone', max_length=30)
    email = models.EmailField('Email', blank=True, null=True)
    address = models.TextField('Delivery address')
    comment = models.TextField('Order notes', blank=True, default='')
    created_at = models.DateTimeField('Order date', auto_now_add=True)
    status = models.CharField('Status', max_length=20, choices=STATUS_CHOICES, default='pending')

    @property
    def total(self):
        return sum(item.total for item in self.items.all())

    class Meta:
        verbose_name = 'Order'
        verbose_name_plural = 'Orders'
        ordering = ['-created_at']

    def __str__(self):
        return f'Order #{self.pk} - {self.full_name}'


class OrderItem(models.Model):
    order = models.ForeignKey(Order, related_name='items', on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.PROTECT)
    quantity = models.PositiveIntegerField('Quantity', default=1)
    price = models.DecimalField('Price', max_digits=10, decimal_places=2)

    @property
    def total(self):
        return self.price * self.quantity

    class Meta:
        verbose_name = 'Order item'
        verbose_name_plural = 'Order items'

    def __str__(self):
        return f'{self.product.name} x {self.quantity}'
