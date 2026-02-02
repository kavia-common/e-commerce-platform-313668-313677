from django import forms

from contact.models import ContactMessage


class LoggedInContactForm(forms.ModelForm):
    """Contact form for logged-in users (message only)."""

    class Meta:
        model = ContactMessage
        fields = ("message",)
        widgets = {"message": forms.Textarea(attrs={"class": "form-control", "rows": 4})}


class GuestContactForm(forms.ModelForm):
    """Contact form for guests (name/email/phone + message)."""

    class Meta:
        model = ContactMessage
        fields = ("name", "email", "phone", "message")
        widgets = {
            "name": forms.TextInput(attrs={"class": "form-control"}),
            "email": forms.EmailInput(attrs={"class": "form-control"}),
            "phone": forms.TextInput(attrs={"class": "form-control"}),
            "message": forms.Textarea(attrs={"class": "form-control", "rows": 4}),
        }
