from django.contrib import admin

from accounts.models import CustomerProfile


@admin.register(CustomerProfile)
class CustomerProfileAdmin(admin.ModelAdmin):
    list_display = ("user", "full_name", "phone_number")
    search_fields = ("user__username", "full_name", "phone_number")
