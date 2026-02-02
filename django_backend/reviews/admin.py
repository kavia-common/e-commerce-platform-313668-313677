from django.contrib import admin

from reviews.models import Review


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ("product", "author", "created_at")
    search_fields = ("product__name", "author__username", "body")
    list_filter = ("created_at",)
