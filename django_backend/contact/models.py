from django.conf import settings
from django.db import models


class ContactMessage(models.Model):
    """
    Contact messages submitted by guests or logged-in users.

    PDF requirement: guest form collects name/email/phone + message; logged-in form collects message only.
    """

    user = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, blank=True, on_delete=models.SET_NULL, related_name="contact_messages")
    name = models.CharField(max_length=200, blank=True)
    email = models.EmailField(blank=True)
    phone = models.CharField(max_length=30, blank=True)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return f"ContactMessage({self.id})"
