from django.urls import path

from accounts.views import PasswordChange, login_view, logout_view, register_view

app_name = "accounts"

urlpatterns = [
    path("register/", register_view, name="register"),
    path("login/", login_view, name="login"),
    path("logout/", logout_view, name="logout"),
    path("password/change/", PasswordChange.as_view(), name="password_change"),
]
