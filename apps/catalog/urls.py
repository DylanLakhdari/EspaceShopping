from django.urls import path
from.views import index, product_detail

urlpatterns = [
    path("", index, name="catalog-index"),
    path("product/<str:slug>/", product_detail, name="catalog-product")
]
