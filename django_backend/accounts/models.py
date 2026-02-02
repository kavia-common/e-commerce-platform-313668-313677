from django.conf import settings
from django.db import models


class CustomerProfile(models.Model):
    """
    Optional extension for customer data beyond django.contrib.auth.User.

    The PDF narrative does not strictly define required profile fields, but the appendix mentions
    full name, phone, and email. We store them here as optional fields.
    """

    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="profile")
    full_name = models.CharField(max_length=200, blank=True)
    phone_number = models.CharField(max_length=30, blank=True)

    def __str__(self) -> str:
        return f"Profile({self.user.username})"
