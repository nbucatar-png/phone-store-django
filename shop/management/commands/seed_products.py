from django.core.management.base import BaseCommand

from shop.models import Product


class Command(BaseCommand):
    help = 'Populate the catalog with demo products'

    def handle(self, *args, **options):
        products = [
            {'brand': 'Apple', 'name': 'iPhone 15 Pro', 'category': 'phone', 'price': 999, 'image_url': 'https://images.unsplash.com/photo-1592750475338-74b7b21085ab?auto=format&fit=crop&w=900&q=80', 'description': 'A powerful Apple smartphone with a fast chip, advanced camera system, and bright OLED display.', 'stock': 15, 'featured': True},
            {'brand': 'Samsung', 'name': 'Galaxy S24 Ultra', 'category': 'phone', 'price': 1099, 'image_url': 'https://images.unsplash.com/photo-1511707171634-5f897ff02aa9?auto=format&fit=crop&w=900&q=80', 'description': 'A premium smartphone with a large display, versatile camera, and all-day battery life.', 'stock': 12, 'featured': True},
            {'brand': 'Xiaomi', 'name': 'Redmi Note 13 Pro', 'category': 'phone', 'price': 399, 'image_url': 'https://images.unsplash.com/photo-1580910051074-3eb694886505?auto=format&fit=crop&w=900&q=80', 'description': 'A reliable smartphone with a vivid display, strong battery, and smooth everyday performance.', 'stock': 18, 'featured': True},
            {'brand': 'Apple', 'name': 'AirPods Pro 2', 'category': 'accessory', 'price': 249, 'image_url': 'https://images.unsplash.com/photo-1606220588913-b3aacb4d2f46?auto=format&fit=crop&w=900&q=80', 'description': 'Wireless earbuds with active noise cancellation and rich, detailed sound.', 'stock': 25, 'featured': True},
            {'brand': 'Samsung', 'name': 'Armor Case', 'category': 'accessory', 'price': 29, 'image_url': 'https://images.unsplash.com/photo-1523275335684-37898b6baf30?auto=format&fit=crop&w=900&q=80', 'description': 'A durable case designed to protect your phone from drops and scratches.', 'stock': 40, 'featured': False},
            {'brand': 'Baseus', 'name': '65W Charger', 'category': 'accessory', 'price': 49, 'image_url': 'https://images.unsplash.com/photo-1554415707-6e8cfc93fe23?auto=format&fit=crop&w=900&q=80', 'description': 'Fast USB-C charging for phones, tablets, and other compatible devices.', 'stock': 30, 'featured': False},
        ]
        for item in products:
            Product.objects.update_or_create(brand=item['brand'], name=item['name'], defaults=item)
        self.stdout.write(self.style.SUCCESS('Demo catalog populated successfully.'))
