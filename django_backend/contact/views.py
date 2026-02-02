from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import HttpRequest, HttpResponse
from django.shortcuts import redirect, render
from django.views.decorators.http import require_http_methods

from contact.forms import GuestContactForm, LoggedInContactForm


# PUBLIC_INTERFACE
@require_http_methods(["GET", "POST"])
def contact_entrypoint(request: HttpRequest) -> HttpResponse:
    """
    Contact page entrypoint.

    If user is authenticated -> logged-in form; else -> guest form.
    PDF: login is not mandatory to report a problem/query.
    """
    if request.user.is_authenticated:
        return contact_logged_in(request)
    return contact_guest(request)


# PUBLIC_INTERFACE
@login_required
@require_http_methods(["GET", "POST"])
def contact_logged_in(request: HttpRequest) -> HttpResponse:
    """Logged-in contact form: message only."""
    form = LoggedInContactForm(request.POST or None)
    if request.method == "POST" and form.is_valid():
        msg = form.save(commit=False)
        msg.user = request.user
        msg.save()
        messages.success(request, "Your message has been submitted to the admin.")
        return redirect("contact:contact")
    return render(request, "contact/contact_logged_in.html", {"form": form})


# PUBLIC_INTERFACE
@require_http_methods(["GET", "POST"])
def contact_guest(request: HttpRequest) -> HttpResponse:
    """Guest contact form: name/email/phone + message."""
    form = GuestContactForm(request.POST or None)
    if request.method == "POST" and form.is_valid():
        form.save()
        messages.success(request, "Your message has been submitted to the admin.")
        return redirect("contact:contact_guest")
    return render(request, "contact/contact_guest.html", {"form": form})
