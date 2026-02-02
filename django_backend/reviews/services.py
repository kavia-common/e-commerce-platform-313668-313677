from django.contrib.auth.models import AbstractBaseUser

from catalog.models import Product
from orders.models import OrderItem


# PUBLIC_INTERFACE
def user_can_review_product(user: AbstractBaseUser, product: Product) -> bool:
    """
    Determine whether a user can review a product.

    The PDF states "only customers who bought the specific product can write a review", but does not specify
    enforcement. As a conservative implementation aligned with the architecture doc, we require at least one
    order item for that user/product.
    """
    if not getattr(user, "is_authenticated", False):
        return False
    return OrderItem.objects.filter(order__user=user, product=product).exists()
