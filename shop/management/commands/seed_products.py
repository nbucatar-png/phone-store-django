from django.core.management.base import BaseCommand

from shop.models import Product


class Command(BaseCommand):
    help = 'Заполняет каталог тестовыми товарами'

    def handle(self, *args, **options):
        products = [
            {
                'brand': 'Apple',
                'name': 'iPhone 15 Pro',
                'category': 'phone',
                'price': 119000,
                'image_url': 'https://images.unsplash.com/photo-1592750475338-74b7b21085ab?auto=format&fit=crop&w=900&q=80',
                'description': 'Флагманский смартфон Apple с мощным чипом, отличной камерой и OLED-экраном.',
                'stock': 15,
                'featured': True,
            },
            {
                'brand': 'Samsung',
                'name': 'Galaxy S24 Ultra',
                'category': 'phone',
                'price': 109000,
                'image_url': 'https://images.unsplash.com/photo-1511707171634-5f897ff02aa9?auto=format&fit=crop&w=900&q=80',
                'description': 'Мощный смартфон с большим экраном, 200 МП камерой и долгим временем автономной работы.',
                'stock': 12,
                'featured': True,
            },
            {
                'brand': 'Xiaomi',
                'name': 'Redmi Note 13 Pro',
                'category': 'phone',
                'price': 39900,
                'image_url': 'https://images.unsplash.com/photo-1580910051074-3eb694886505?auto=format&fit=crop&w=900&q=80',
                'description': 'Удобный смартфон с ярким дисплеем, хорошей автономностью и мощной батареей.',
                'stock': 18,
                'featured': True,
            },
            {
                'brand': 'Apple',
                'name': 'AirPods Pro 2',
                'category': 'accessory',
                'price': 16990,
                'image_url': 'https://images.unsplash.com/photo-1606220588913-b3aacb4d2f46?auto=format&fit=crop&w=900&q=80',
                'description': 'Беспроводные наушники с активным шумоподавлением и качественным звуком.',
                'stock': 25,
                'featured': True,
            },
            {
                'brand': 'Samsung',
                'name': 'Чехол Armor Case',
                'category': 'accessory',
                'price': 1490,
                'image_url': 'https://images.unsplash.com/photo-1523275335684-37898b6baf30?auto=format&fit=crop&w=900&q=80',
                'description': 'Надёжный чехол для защиты телефона от ударов и царапин.',
                'stock': 40,
                'featured': False,
            },
            {
                'brand': 'Baseus',
                'name': 'Зарядное устройство 65W',
                'category': 'accessory',
                'price': 2790,
                'image_url': 'https://images.unsplash.com/photo-1554415707-6e8cfc93fe23?auto=format&fit=crop&w=900&q=80',
                'description': 'Быстрая зарядка для смартфонов и планшетов с поддержкой USB-C.',
                'stock': 30,
                'featured': False,
            },
        ]

        for item in products:
            Product.objects.update_or_create(
                brand=item['brand'],
                name=item['name'],
                defaults={
                    'category': item['category'],
                    'price': item['price'],
                    'image_url': item['image_url'],
                    'description': item['description'],
                    'stock': item['stock'],
                    'featured': item['featured'],
                }
            )

        self.stdout.write(self.style.SUCCESS('Каталог наполнился товарами!'))
