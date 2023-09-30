from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path("", views.homepage, name="homepage"),
    path("products", views.index, name="products"),
    path("login", views.login, name="login"),
    path("logout", views.logoutuser, name="logout"),
    path("register", views.register, name="register"),
    path("AccountSetting", views.AccountSetting, name="AccountSetting"),
    path("product/<slug:slug>", views.product_detail, name="product_detail"),
    path("products/<slug:category_slug>", views.showproducts, name="showproducts"),
    path("FAQ", views.FAQ, name="FAQ"),
    path("editprofile", views.editprofile, name="editprofile"),
    path("favorites", views.favorites, name="favorites"),
    path("product-list", views.productlistajax, name="product-list"),
    path("searchproduct", views.searchproduct, name="searchproduct")

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
