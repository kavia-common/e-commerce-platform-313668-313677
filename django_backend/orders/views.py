from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from django.views.decorators.http import require_http_methods

from cart.models import CartItem
from orders.forms import CheckoutForm, TrackOrderForm
from orders.models import Order
from orders.services import create_order_from_cart


# PUBLIC_INTERFACE
@login_required
@require_http_methods(["GET", "POST"])
def checkout_view(request: HttpRequest) -> HttpResponse:
    """Checkout page: delivery details + payment mode; place order and show Order ID (PDF requirement)."""
    items = CartItem.objects.select_related("product").filter(cart__user=request.user).order_by("id")
    total = sum((i.product.price * i.quantity) for i in items)

    if request.method == "POST":
        form = CheckoutForm(request.POST)
        if form.is_valid():
            try:
                order = create_order_from_cart(user=request.user, checkout_data=form.cleaned_data)
            except ValueError:
                messages.error(request, "Your cart is empty.")
                form = CheckoutForm()
            else:
                # PDF says: show a pop-up with order id and redirect to home page
                messages.success(request, f"Order placed successfully. Your Order ID is {order.order_id}.")
                return render(request, "orders/order_success.html", {"order": order})
        else:
            messages.error(request, "Please correct the errors in the checkout form.")
    else:
        form = CheckoutForm()

    return render(request, "orders/checkout.html", {"form": form, "items": items, "total": total})


# PUBLIC_INTERFACE
@require_http_methods(["GET", "POST"])
def track_order_view(request: HttpRequest) -> HttpResponse:
    """
    Track order by Order ID.

    The PDF does not explicitly require login for tracking, so this is available to anyone with the Order ID.
    """
    order = None
    form = TrackOrderForm(request.POST or None)
    if request.method == "POST" and form.is_valid():
        order_id = form.cleaned_data["order_id"]
        try:
            order = Order.objects.prefetch_related("items__product").select_related("user").get(order_id=order_id)
        except Order.DoesNotExist:
            messages.error(request, "Order not found. Please check the Order ID.")
            order = None

    return render(request, "orders/track_order.html", {"form": form, "order": order})
