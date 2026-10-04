from decimal import Decimal

from django.db.models import Q
from django.shortcuts import redirect, render
from django.urls import reverse

from .forms import CheckoutForm
from .models import Order, OrderItem, Product


def get_cart_data(request):
    cart = request.session.get('cart', {})
    products = Product.objects.filter(id__in=[int(pid) for pid in cart.keys()])
    cart_items = []
    total = Decimal('0')

    for product in products:
        quantity = int(cart.get(str(product.id), 0))
        if quantity <= 0:
            continue
        item_total = product.price * quantity
        total += item_total
        cart_items.append({
            'product': product,
            'quantity': quantity,
            'item_total': item_total,
        })

    return cart_items, total


def home(request):
    products = Product.objects.filter(featured=True)[:6]
    return render(request, 'shop/home.html', {'products': products})


def catalog(request):
    category = request.GET.get('category', '')
    if category:
        products = Product.objects.filter(category=category)
    else:
        products = Product.objects.all()
    return render(request, 'shop/catalog.html', {'products': products, 'selected_category': category})


def product_detail(request, pk):
    product = Product.objects.get(pk=pk)
    return render(request, 'shop/product_detail.html', {'product': product})


def add_to_cart(request, product_id):
    product = Product.objects.get(pk=product_id)
    cart = request.session.get('cart', {})
    quantity = int(request.POST.get('quantity', 1))
    if quantity < 1:
        quantity = 1
    cart[str(product.id)] = cart.get(str(product.id), 0) + quantity
    request.session['cart'] = cart
    return redirect('cart')


def cart(request):
    cart_items, total = get_cart_data(request)
    return render(request, 'shop/cart.html', {'cart_items': cart_items, 'total': total})


def checkout(request):
    cart_items, total = get_cart_data(request)
    if not cart_items:
        return redirect('cart')

    if request.method == 'POST':
        form = CheckoutForm(request.POST)
        if form.is_valid():
            order = Order.objects.create(
                full_name=form.cleaned_data['full_name'],
                phone=form.cleaned_data['phone'],
                email=form.cleaned_data.get('email') or '',
                address=form.cleaned_data['address'],
                comment=form.cleaned_data.get('comment') or '',
            )

            for item in cart_items:
                OrderItem.objects.create(
                    order=order,
                    product=item['product'],
                    quantity=item['quantity'],
                    price=item['product'].price,
                )

            request.session['cart'] = {}
            return redirect('order_success', order_id=order.id)
    else:
        form = CheckoutForm()

    return render(request, 'shop/checkout.html', {'form': form, 'cart_items': cart_items, 'total': total})


def order_success(request, order_id):
    order = Order.objects.get(pk=order_id)
    return render(request, 'shop/order_success.html', {'order': order})
