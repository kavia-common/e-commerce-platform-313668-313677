from django.contrib import admin

from catalog.models import Product, ProductFeature


class ProductFeatureInline(admin.TabularInline):
    model = ProductFeature
    extra = 1


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ("name", "price", "created_at", "updated_at")
    search_fields = ("name",)
    inlines = [ProductFeatureInline]


@admin.register(ProductFeature)
class ProductFeatureAdmin(admin.ModelAdmin):
    list_display = ("product", "text")
    search_fields = ("product__name", "text")
