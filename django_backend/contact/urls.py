from django.urls import path

from contact.views import contact_entrypoint, contact_guest

app_name = "contact"

urlpatterns = [
    path("contact/", contact_entrypoint, name="contact"),
    path("contact/guest/", contact_guest, name="contact_guest"),
]
