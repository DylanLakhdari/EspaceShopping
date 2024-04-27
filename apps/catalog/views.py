from django.shortcuts import get_object_or_404, render
from .models import Product

def index(request):
    products = Product.objects.all()

    return render(request, "catalog/index.html", context={"products": products})

def product_detail(request, slug):

    products = get_object_or_404(Product, slug=slug)

    return render(request, "catalog/product_detail.html", context={"products": products})