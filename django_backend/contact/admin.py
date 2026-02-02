from django.contrib import admin

from contact.models import ContactMessage


@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ("id", "user", "name", "email", "phone", "created_at")
    search_fields = ("name", "email", "phone", "message", "user__username")
    list_filter = ("created_at",)
    readonly_fields = ("created_at",)
