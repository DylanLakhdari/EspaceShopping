from django.urls import path
from.views import index, product_detail, add_to_cart, cart, delete_cart, delete_order

urlpatterns = [
    path("", index, name="catalog-index"),
    path("product/<str:slug>/", product_detail, name="catalog-product"),
    path("product/<str:slug>/add-to-cart/", add_to_cart, name="catalog-add-to-cart"),
    path("cart/", cart, name="catalog-cart"),
    path("cart/delete/", delete_cart, name='catalog-delete-cart'),
    path("cart/order/delete/<int:order_id>", delete_order, name="catalog-delete-cart-order"),
]
