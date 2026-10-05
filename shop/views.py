from decimal import Decimal, InvalidOperation

from django.db.models import Q
from django.shortcuts import get_object_or_404, redirect, render

from .forms import CheckoutForm
from .models import Order, OrderItem, Product


def get_cart_data(request):
    cart = request.session.get('cart', {})
    product_ids = []
    for product_id in cart:
        try:
            product_ids.append(int(product_id))
        except (TypeError, ValueError):
            continue
    products = Product.objects.filter(id__in=product_ids)
    cart_items, total = [], Decimal('0')
    cleaned_cart = {}
    for product in products:
        try:
            quantity = max(0, int(cart.get(str(product.id), 0)))
        except (TypeError, ValueError):
            quantity = 0
        quantity = min(quantity, product.stock)
        if quantity:
            cleaned_cart[str(product.id)] = quantity
            item_total = product.price * quantity
            total += item_total
            cart_items.append({'product': product, 'quantity': quantity, 'item_total': item_total})
    if cleaned_cart != cart:
        request.session['cart'] = cleaned_cart
    return cart_items, total


def home(request):
    products = Product.objects.filter(featured=True, stock__gt=0)[:6]
    return render(request, 'shop/home.html', {'products': products})


def catalog(request):
    category = request.GET.get('category', '').strip()
    search_query = request.GET.get('q', '').strip()
    products = Product.objects.filter(stock__gt=0)
    if category in {'phone', 'accessory'}:
        products = products.filter(category=category)
    else:
        category = ''
    if search_query:
        products = products.filter(Q(brand__icontains=search_query) | Q(name__icontains=search_query) | Q(description__icontains=search_query))
    return render(request, 'shop/catalog.html', {'products': products, 'selected_category': category, 'search_query': search_query})


def product_detail(request, pk):
    return render(request, 'shop/product_detail.html', {'product': get_object_or_404(Product, pk=pk)})


def add_to_cart(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    if request.method == 'POST' and product.stock > 0:
        try:
            quantity = max(1, int(request.POST.get('quantity', 1)))
        except (TypeError, ValueError):
            quantity = 1
        cart = request.session.get('cart', {})
        current = int(cart.get(str(product.id), 0))
        cart[str(product.id)] = min(current + quantity, product.stock)
        request.session['cart'] = cart
    return redirect('cart')


def update_cart(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    if request.method == 'POST':
        try:
            quantity = max(0, min(int(request.POST.get('quantity', 0)), product.stock))
        except (TypeError, ValueError):
            quantity = 0
        cart = request.session.get('cart', {})
        if quantity:
            cart[str(product.id)] = quantity
        else:
            cart.pop(str(product.id), None)
        request.session['cart'] = cart
    return redirect('cart')


def remove_from_cart(request, product_id):
    cart = request.session.get('cart', {})
    cart.pop(str(product_id), None)
    request.session['cart'] = cart
    return redirect('cart')


def cart(request):
    cart_items, total = get_cart_data(request)
    return render(request, 'shop/cart.html', {'cart_items': cart_items, 'total': total})


def checkout(request):
    cart_items, total = get_cart_data(request)
    if not cart_items:
        return redirect('cart')
    form = CheckoutForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        order = Order.objects.create(full_name=form.cleaned_data['full_name'], phone=form.cleaned_data['phone'], email=form.cleaned_data.get('email') or '', address=form.cleaned_data['address'], comment=form.cleaned_data.get('comment') or '')
        for item in cart_items:
            OrderItem.objects.create(order=order, product=item['product'], quantity=item['quantity'], price=item['product'].price)
        request.session['cart'] = {}
        return redirect('order_success', order_id=order.id)
    return render(request, 'shop/checkout.html', {'form': form, 'cart_items': cart_items, 'total': total})


def order_success(request, order_id):
    return render(request, 'shop/order_success.html', {'order': get_object_or_404(Order, pk=order_id)})
