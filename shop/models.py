from django.contrib import admin
from django.db import models


class Product(models.Model):
    CATEGORY_CHOICES = [
        ('phone', 'Телефон'),
        ('accessory', 'Аксессуар'),
    ]

    category = models.CharField('Категория', max_length=20, choices=CATEGORY_CHOICES, default='phone')
    brand = models.CharField('Бренд', max_length=100)
    name = models.CharField('Название', max_length=200)
    description = models.TextField('Описание')
    price = models.DecimalField('Цена', max_digits=10, decimal_places=2)
    image_url = models.URLField('Ссылка на изображение', max_length=500, blank=True)
    stock = models.PositiveIntegerField('На складе', default=1)
    featured = models.BooleanField('Показать на главной', default=False)
    created_at = models.DateTimeField('Создан', auto_now_add=True)

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'
        ordering = ['-created_at']

    def __str__(self):
        return f'{self.brand} {self.name}'


class Order(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Ожидает'),
        ('processed', 'В обработке'),
        ('completed', 'Завершён'),
    ]

    full_name = models.CharField('Имя', max_length=200)
    phone = models.CharField('Телефон', max_length=30)
    email = models.EmailField('Email', blank=True, null=True)
    address = models.TextField('Адрес доставки')
    comment = models.TextField('Комментарий', blank=True, default='')
    created_at = models.DateTimeField('Дата заказа', auto_now_add=True)
    status = models.CharField('Статус', max_length=20, choices=STATUS_CHOICES, default='pending')

    @property
    def total(self):
        return sum(item.total for item in self.items.all())

    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'
        ordering = ['-created_at']

    def __str__(self):
        return f'Заказ #{self.pk} - {self.full_name}'


class OrderItem(models.Model):
    order = models.ForeignKey(Order, related_name='items', on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.PROTECT)
    quantity = models.PositiveIntegerField('Количество', default=1)
    price = models.DecimalField('Цена', max_digits=10, decimal_places=2)

    @property
    def total(self):
        return self.price * self.quantity

    class Meta:
        verbose_name = 'Позиция заказа'
        verbose_name_plural = 'Позиции заказов'

    def __str__(self):
        return f'{self.product.name} x {self.quantity}'
