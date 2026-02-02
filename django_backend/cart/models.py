from django.conf import settings
from django.db import models
from django.db.models import UniqueConstraint


class Cart(models.Model):
    """A persisted cart for a logged-in user (architecture decision)."""

    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="cart")
    created_at = models.DateTimeField(auto_now_add=True)  # optional per architecture
    updated_at = models.DateTimeField(auto_now=True)  # optional per architecture

    def __str__(self) -> str:
        return f"Cart({self.user.username})"


class CartItem(models.Model):
    """A line item inside a cart."""

    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, related_name="items")
    product = models.ForeignKey("catalog.Product", on_delete=models.CASCADE, related_name="cart_items")
    quantity = models.PositiveIntegerField(default=1)

    class Meta:
        constraints = [UniqueConstraint(fields=["cart", "product"], name="uniq_cart_product")]

    def __str__(self) -> str:
        return f"CartItem({self.cart_id}, {self.product_id}, qty={self.quantity})"
