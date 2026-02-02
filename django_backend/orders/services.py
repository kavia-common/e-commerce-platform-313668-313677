from django.db import transaction

from cart.models import CartItem
from orders.models import Order, OrderItem


# PUBLIC_INTERFACE
@transaction.atomic
def create_order_from_cart(*, user, checkout_data: dict) -> Order:
    """
    Create an Order + OrderItems from the current user's cart items and then empty the cart.

    PDF requirement: cart is emptied after successful checkout and an Order ID is shown.
    """
    cart_items = CartItem.objects.select_related("product", "cart").filter(cart__user=user).order_by("id")
    if not cart_items.exists():
        raise ValueError("Cart is empty")

    order = Order.objects.create(
        user=user,
        order_id=Order.generate_order_id(),
        payment_mode=checkout_data["payment_mode"],
        address=checkout_data["address"],
        city=checkout_data["city"],
        state=checkout_data["state"],
        zipcode=checkout_data["zipcode"],
        contact_number=checkout_data["contact_number"],
    )

    OrderItem.objects.bulk_create(
        [
            OrderItem(
                order=order,
                product=ci.product,
                quantity=ci.quantity,
                unit_price=ci.product.price,
            )
            for ci in cart_items
        ]
    )

    # Empty cart after successful checkout
    cart_items.delete()
    return order
