from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import HttpRequest, HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.views.decorators.http import require_GET, require_POST

from cart.models import CartItem
from cart.services import add_product, change_quantity, get_or_create_cart_for_user
from catalog.models import Product


# PUBLIC_INTERFACE
@login_required
@require_GET
def view_cart(request: HttpRequest) -> HttpResponse:
    """Display the user's cart and allow quantity adjustments."""
    cart = get_or_create_cart_for_user(request.user)
    items = cart.items.select_related("product").order_by("id")
    total = sum((i.product.price * i.quantity) for i in items)
    return render(request, "cart/cart.html", {"cart": cart, "items": items, "total": total})


# PUBLIC_INTERFACE
@login_required
@require_POST
def add_to_cart(request: HttpRequest, product_id: int) -> HttpResponse:
    """Add a product to cart; increments quantity if already present."""
    product = get_object_or_404(Product, id=product_id)
    add_product(request.user, product)
    messages.success(request, f"Added '{product.name}' to cart.")
    return redirect(request.META.get("HTTP_REFERER") or "cart:view_cart")


# PUBLIC_INTERFACE
@login_required
@require_POST
def increase_item(request: HttpRequest, item_id: int) -> HttpResponse:
    """Increase cart item quantity by 1."""
    item = get_object_or_404(CartItem, id=item_id, cart__user=request.user)
    change_quantity(item, delta=1)
    return redirect("cart:view_cart")


# PUBLIC_INTERFACE
@login_required
@require_POST
def decrease_item(request: HttpRequest, item_id: int) -> HttpResponse:
    """Decrease cart item quantity by 1; deletes item if quantity becomes 0."""
    item = get_object_or_404(CartItem, id=item_id, cart__user=request.user)
    change_quantity(item, delta=-1)
    return redirect("cart:view_cart")
