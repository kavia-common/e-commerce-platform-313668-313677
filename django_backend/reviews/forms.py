from django import forms

from reviews.models import Review


class ReviewForm(forms.ModelForm):
    """Form for creating a product review."""

    class Meta:
        model = Review
        fields = ("body",)
        widgets = {"body": forms.Textarea(attrs={"class": "form-control", "rows": 4})}
