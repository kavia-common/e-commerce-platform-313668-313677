from django import forms

from orders.models import Order


class CheckoutForm(forms.Form):
    """Collect delivery details and payment mode at checkout (PDF requirement)."""

    PAYMENT_MODE_CHOICES = [
        ("COD", "Cash on Delivery"),
        ("CARD", "Card"),
        ("UPI", "UPI"),
    ]
    # Payment modes are not specified in PDF; we must store a choice. These are generic and can be adjusted.

    address = forms.CharField(widget=forms.Textarea(attrs={"class": "form-control", "rows": 3}))
    city = forms.CharField(widget=forms.TextInput(attrs={"class": "form-control"}))
    state = forms.CharField(widget=forms.TextInput(attrs={"class": "form-control"}))
    zipcode = forms.CharField(widget=forms.TextInput(attrs={"class": "form-control"}))
    contact_number = forms.CharField(widget=forms.TextInput(attrs={"class": "form-control"}))
    payment_mode = forms.ChoiceField(choices=PAYMENT_MODE_CHOICES, widget=forms.Select(attrs={"class": "form-select"}))


class TrackOrderForm(forms.Form):
    """Order tracking input form (Order ID)."""

    order_id = forms.CharField(widget=forms.TextInput(attrs={"class": "form-control"}))

    # PUBLIC_INTERFACE
    def clean_order_id(self) -> str:
        """Normalize order ID input."""
        return (self.cleaned_data["order_id"] or "").strip().upper()
