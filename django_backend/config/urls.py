"""
Project URL configuration.

Routes are server-rendered pages (PDF-aligned). Django Admin is enabled for product and data management.
"""

from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include(("catalog.urls", "catalog"), namespace="catalog")),
    path("", include(("accounts.urls", "accounts"), namespace="accounts")),
    path("", include(("cart.urls", "cart"), namespace="cart")),
    path("", include(("orders.urls", "orders"), namespace="orders")),
    path("", include(("contact.urls", "contact"), namespace="contact")),
    path("", include(("reviews.urls", "reviews"), namespace="reviews")),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
