from django.conf import settings
from django.db import models


class Review(models.Model):
    """Product review written by a user."""

    product = models.ForeignKey("catalog.Product", on_delete=models.CASCADE, related_name="reviews")
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="reviews")
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)  # optional per architecture

    class Meta:
        ordering = ["-created_at", "-id"]
        unique_together = ("product", "author")  # not specified; helps prevent spam duplicates; acceptable constraint

    def __str__(self) -> str:
        return f"Review({self.product_id}, {self.author_id})"
