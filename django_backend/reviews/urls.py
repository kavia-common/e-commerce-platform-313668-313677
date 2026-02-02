from django.urls import path

from reviews.views import create_review

app_name = "reviews"

urlpatterns = [
    path("products/<int:product_id>/reviews/", create_review, name="create"),
]
