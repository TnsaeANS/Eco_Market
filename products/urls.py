from django.urls import path
from . import views




urlpatterns = [
    path('', views.homepage),
    path('products', views.index),
    path('login', views.login),
    path('register', views.register)
]
