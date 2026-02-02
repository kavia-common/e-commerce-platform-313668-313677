from django.urls import path

from catalog.views import home_view, product_detail_view, search_view

app_name = "catalog"

urlpatterns = [
    path("", home_view, name="home"),
    path("search/", search_view, name="search"),
    path("products/<int:product_id>/", product_detail_view, name="product_detail"),
]
