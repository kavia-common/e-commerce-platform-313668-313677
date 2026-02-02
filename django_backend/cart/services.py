from django.contrib.auth.models import AbstractBaseUser
from django.db import transaction

from cart.models import Cart, CartItem
from catalog.models import Product


# PUBLIC_INTERFACE
def get_or_create_cart_for_user(user: AbstractBaseUser) -> Cart:
    """Get or create the persisted cart for a logged-in user."""
    cart, _ = Cart.objects.get_or_create(user=user)
    return cart


# PUBLIC_INTERFACE
@transaction.atomic
def add_product(user: AbstractBaseUser, product: Product) -> CartItem:
    """Add a product to the user's cart or increment quantity if it already exists."""
    cart = get_or_create_cart_for_user(user)
    item, created = CartItem.objects.get_or_create(cart=cart, product=product, defaults={"quantity": 1})
    if not created:
        item.quantity += 1
        item.save(update_fields=["quantity"])
    return item


# PUBLIC_INTERFACE
@transaction.atomic
def change_quantity(item: CartItem, delta: int) -> None:
    """Increase/decrease quantity for a cart item; removes item if quantity reaches 0."""
    new_qty = int(item.quantity) + int(delta)
    if new_qty <= 0:
        item.delete()
        return
    item.quantity = new_qty
    item.save(update_fields=["quantity"])
