from django.urls import path

from orders.views import checkout_view, track_order_view

app_name = "orders"

urlpatterns = [
    path("checkout/", checkout_view, name="checkout"),
    path("track-order/", track_order_view, name="track_order"),
]
