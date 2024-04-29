from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse
from .models import Product, Order, Cart

def index(request):
    products = Product.objects.all()

    return render(request, "catalog/index.html", context={"products": products})

def product_detail(request, slug):

    products = get_object_or_404(Product, slug=slug)

    return render(request, "catalog/product_detail.html", context={"products": products})

def add_to_cart(request, slug):
    user = request.user
    product = get_object_or_404(Product, slug=slug)
    cart, _ = Cart.objects.get_or_create(user=user)
    order, created = Order.objects.get_or_create(user = user, product=product)

    if created:
        cart.orders.add(order)
        cart.save()
    else:
        order.quantity += 1
        order.save()
    
    return redirect(reverse("product"), kwargs=slug)
    