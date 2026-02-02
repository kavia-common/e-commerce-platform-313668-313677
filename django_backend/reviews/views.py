from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import HttpRequest, HttpResponse
from django.shortcuts import get_object_or_404, redirect
from django.views.decorators.http import require_POST

from catalog.models import Product
from reviews.forms import ReviewForm
from reviews.services import user_can_review_product


# PUBLIC_INTERFACE
@login_required
@require_POST
def create_review(request: HttpRequest, product_id: int) -> HttpResponse:
    """Create a review for a product if user has ordered it."""
    product = get_object_or_404(Product, id=product_id)
    if not user_can_review_product(request.user, product):
        messages.error(request, "You can only review products you have ordered.")
        return redirect("catalog:product_detail", product_id=product.id)

    form = ReviewForm(request.POST)
    if not form.is_valid():
        messages.error(request, "Please correct the errors in the review form.")
        return redirect("catalog:product_detail", product_id=product.id)

    review = form.save(commit=False)
    review.product = product
    review.author = request.user
    review.save()

    messages.success(request, "Review submitted.")
    return redirect("catalog:product_detail", product_id=product.id)
