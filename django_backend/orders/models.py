import uuid

from django.conf import settings
from django.db import models


class Order(models.Model):
    """
    Order placed at checkout.

    PDF requirements: delivery details + payment mode, generate Order ID, and track by Order ID.
    Order status values are not specified; we store a simple status string for tracking display.
    """

    class Status(models.TextChoices):
        PLACED = "PLACED", "Placed"
        PROCESSING = "PROCESSING", "Processing"
        SHIPPED = "SHIPPED", "Shipped"
        DELIVERED = "DELIVERED", "Delivered"

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="orders")
    order_id = models.CharField(max_length=32, unique=True, db_index=True)
    payment_mode = models.CharField(max_length=50)

    address = models.TextField()
    city = models.CharField(max_length=120)
    state = models.CharField(max_length=120)
    zipcode = models.CharField(max_length=20)
    contact_number = models.CharField(max_length=30)

    status = models.CharField(max_length=20, choices=Status.choices, default=Status.PLACED)
    created_at = models.DateTimeField(auto_now_add=True)

    # PUBLIC_INTERFACE
    @staticmethod
    def generate_order_id() -> str:
        """Generate an order identifier shown to the user (PDF requirement)."""
        return uuid.uuid4().hex[:12].upper()

    def __str__(self) -> str:
        return f"Order({self.order_id})"


class OrderItem(models.Model):
    """Line items for an order."""

    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name="items")
    product = models.ForeignKey("catalog.Product", on_delete=models.PROTECT, related_name="order_items")
    quantity = models.PositiveIntegerField()
    unit_price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self) -> str:
        return f"OrderItem({self.order_id}, {self.product_id})"
