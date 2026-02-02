from django.db.models import Q
from django.http import HttpRequest, HttpResponse
from django.shortcuts import get_object_or_404, render
from django.views.decorators.http import require_GET

from catalog.models import Product
from reviews.forms import ReviewForm
from reviews.services import user_can_review_product


# PUBLIC_INTERFACE
@require_GET
def home_view(request: HttpRequest) -> HttpResponse:
    """Home page: list products with image, name, price (PDF requirement)."""
    products = Product.objects.all().order_by("-id")
    return render(request, "catalog/home.html", {"products": products})


# PUBLIC_INTERFACE
@require_GET
def search_view(request: HttpRequest) -> HttpResponse:
    """Search products by name using the navbar search input."""
    q = (request.GET.get("q") or "").strip()
    products = Product.objects.none()
    if q:
        products = Product.objects.filter(Q(name__icontains=q)).order_by("-id")
    return render(request, "catalog/search.html", {"products": products, "q": q})


# PUBLIC_INTERFACE
def product_detail_view(request: HttpRequest, product_id: int) -> HttpResponse:
    """Product detail page: show features and reviews, and allow adding to cart when logged in."""
    product = get_object_or_404(Product, id=product_id)
    reviews_qs = product.reviews.select_related("author").order_by("-created_at", "-id")
    can_review = request.user.is_authenticated and user_can_review_product(request.user, product)
    review_form = ReviewForm() if can_review else None

    return render(
        request,
        "catalog/product_detail.html",
        {
            "product": product,
            "reviews": reviews_qs,
            "can_review": can_review,
            "review_form": review_form,
        },
    )
