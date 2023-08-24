# from django.contrib import admin
# from .models import Product, Offer
# # Register your models here.

# class OfferAdmin(admin.ModelAdmin):
#     list_display = ('code', 'description', 'discount' )


# class ProductAdmin(admin.ModelAdmin):
#     list_display = ('name', 'price', 'stock')

# admin.site.register(Product, ProductAdmin)
# admin.site.register(Offer, OfferAdmin) 

from django import forms
from django.contrib import admin
from mptt.admin import MPTTModelAdmin

from .models import(
    Category,
    Product,
    ProductImage,
    ProductSpecification,
    ProductSpecificationValue,
    ProductType,
)

admin.site.register(Category, MPTTModelAdmin) 

class ProductSpecificationInline(admin.TabularInline):
    model = ProductSpecification

@admin.register(ProductType)
class ProductTypeAdmin(admin.ModelAdmin):
    inlines=[
        ProductSpecificationInline
    ]

class ProductImageInline(admin.TabularInline):
    model = ProductImage

class ProductSpecificationValueInline(admin.TabularInline):
    model = ProductSpecificationValue

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    inlines= [
        ProductSpecificationValueInline,
        ProductImageInline,
    ]



