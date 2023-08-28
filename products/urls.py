from django.urls import path
from . import views


urlpatterns = [
    path("", views.homepage, name="homepage"),
    path("products", views.index),
    path("login", views.login, name="login"),
    path("register", views.register, name="register"),
    path("AccountSetting", views.AccountSetting, name="AccountSetting"),
]
 