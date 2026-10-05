# PhoneStore

A responsive Django storefront for phones and accessories.

## Features

- English user interface and Django admin labels
- Featured products homepage
- Searchable, filterable catalog
- Product detail pages with stock-aware cart limits
- Editable cart quantities and item removal
- Checkout form and order confirmation
- Responsive layout for mobile and desktop

## Quick start

```bash
pip install -r requirements.txt
python manage.py migrate
python manage.py seed_products
python manage.py runserver
```

Open `http://127.0.0.1:8000/` in your browser. Create an admin account with `python manage.py createsuperuser`, then visit `/admin/`.

## Project structure

- `phone_store/` — Django project settings and URLs
- `shop/` — catalog, cart, checkout, models, views, and templates
- `static/` — CSS and frontend assets
