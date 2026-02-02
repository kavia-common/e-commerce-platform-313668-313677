from django.db import models


class Product(models.Model):
    """
    Product displayed on the home page and in product detail view.

    PDF requirements: name, price, image.
    """

    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to="products/")
    created_at = models.DateTimeField(auto_now_add=True)  # optional (architecture allows)
    updated_at = models.DateTimeField(auto_now=True)  # optional (architecture allows)

    def __str__(self) -> str:
        return self.name


class ProductFeature(models.Model):
    """Key feature text associated with a product."""

    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="features")
    text = models.TextField()

    def __str__(self) -> str:
        return f"Feature({self.product_id})"
