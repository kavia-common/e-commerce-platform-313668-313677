from django import template

register = template.Library()


@register.filter
def mul(value, arg):
    """Multiply value by arg (used for subtotal display)."""
    try:
        return value * arg
    except Exception:
        return ""
