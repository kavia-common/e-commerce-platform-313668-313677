from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.models import User

from accounts.models import CustomerProfile


class RegisterForm(UserCreationForm):
    """
    Registration form using Django's UserCreationForm with optional extra fields.

    Extra fields are not strictly required by the PDF narrative, but referenced in the implementation appendix.
    """

    email = forms.EmailField(required=False)
    full_name = forms.CharField(required=False, max_length=200)
    phone_number = forms.CharField(required=False, max_length=30)

    class Meta(UserCreationForm.Meta):
        model = User
        fields = ("username", "email", "full_name", "phone_number", "password1", "password2")

    # PUBLIC_INTERFACE
    def save(self, commit: bool = True):
        """Create the user and optional CustomerProfile."""
        user = super().save(commit=False)
        user.email = self.cleaned_data.get("email") or ""
        if commit:
            user.save()
            CustomerProfile.objects.update_or_create(
                user=user,
                defaults={
                    "full_name": self.cleaned_data.get("full_name") or "",
                    "phone_number": self.cleaned_data.get("phone_number") or "",
                },
            )
        return user


class LoginForm(AuthenticationForm):
    """Login form (username/password)."""

    username = forms.CharField(widget=forms.TextInput(attrs={"autofocus": True}))
