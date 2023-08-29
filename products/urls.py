from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path("", views.homepage, name="homepage"),
    path("products", views.index),
    path("login", views.login, name="login"),
    path("register", views.register, name="register"),
    path("AccountSetting", views.AccountSetting, name="AccountSetting"),
    path('', views.product_all, name='store_home'),
    path('<slug:slug>', views.product_detail, name='product_detail'),
    path('shop/<slug:category_slug>/', views.category_list, name='category_list'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
 