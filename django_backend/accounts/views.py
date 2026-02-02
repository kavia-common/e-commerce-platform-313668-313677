from django.contrib import messages
from django.contrib.auth import login
from django.contrib.auth.views import PasswordChangeView
from django.http import HttpRequest, HttpResponse
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views.decorators.http import require_http_methods, require_POST

from accounts.forms import LoginForm, RegisterForm


# PUBLIC_INTERFACE
@require_http_methods(["GET", "POST"])
def register_view(request: HttpRequest) -> HttpResponse:
    """Register a new user account."""
    if request.user.is_authenticated:
        return redirect("catalog:home")

    form = RegisterForm(request.POST or None)
    if request.method == "POST" and form.is_valid():
        user = form.save()
        messages.success(request, "Account created. You can now log in.")
        return redirect("accounts:login")

    return render(request, "accounts/register.html", {"form": form})


# PUBLIC_INTERFACE
@require_http_methods(["GET", "POST"])
def login_view(request: HttpRequest) -> HttpResponse:
    """Log a user in using username/password."""
    if request.user.is_authenticated:
        return redirect("catalog:home")

    form = LoginForm(request, data=request.POST or None)
    if request.method == "POST" and form.is_valid():
        login(request, form.get_user())
        messages.success(request, "Logged in successfully.")
        return redirect("catalog:home")

    return render(request, "accounts/login.html", {"form": form})


# PUBLIC_INTERFACE
@require_POST
def logout_view(request: HttpRequest) -> HttpResponse:
    """Log the current user out."""
    from django.contrib.auth import logout

    logout(request)
    messages.success(request, "Logged out.")
    return redirect("catalog:home")


class PasswordChange(PasswordChangeView):
    """Password change page (requires login)."""

    template_name = "accounts/password_change.html"
    success_url = reverse_lazy("catalog:home")

    def form_valid(self, form):
        messages.success(self.request, "Password changed successfully.")
        return super().form_valid(form)
