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
    
    return redirect(reverse("catalog-product", kwargs={"slug": slug}))
    
def cart(request):
    cart = get_object_or_404(Cart, user=request.user)
    
    return render(request, "catalog/cart.html", context={"orders": cart.orders.all(),
                                                         'cart': cart,
                                                        })

def delete_cart(request):
    cart = request.user.cart
    if cart :
        cart.orders.all().delete()
        cart.delete()

    return redirect('catalog-index')

def delete_order(request, order_id):
    order = get_object_or_404(Order, id=order_id)

    if order.user == request.user:
        order.delete()
    else:
        pass

    return redirect('catalog-cart')
