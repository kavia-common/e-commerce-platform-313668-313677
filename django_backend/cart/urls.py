from django.urls import path

from cart.views import add_to_cart, decrease_item, increase_item, view_cart

app_name = "cart"

urlpatterns = [
    path("cart/", view_cart, name="view_cart"),
    path("cart/add/<int:product_id>/", add_to_cart, name="add_to_cart"),
    path("cart/increase/<int:item_id>/", increase_item, name="increase_item"),
    path("cart/decrease/<int:item_id>/", decrease_item, name="decrease_item"),
]
