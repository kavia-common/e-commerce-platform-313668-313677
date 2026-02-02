from cart.models import Cart


# PUBLIC_INTERFACE
def cart_summary(request):
    """Add cart item count to template context for logged-in users."""
    if not getattr(request, "user", None) or not request.user.is_authenticated:
        return {"cart_item_count": 0}

    try:
        cart = Cart.objects.get(user=request.user)
    except Cart.DoesNotExist:
        return {"cart_item_count": 0}

    return {"cart_item_count": cart.items.count()}
