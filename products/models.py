from django.db import models
from django.urls import reverse
from mptt.models import MPTTModel, TreeForeignKey
from django.contrib.auth.models import User

# Create your models here.
# class Product(models.Model):
#     name = models.CharField(max_length=50)
#     price = models.FloatField()
#     stock = models.IntegerField()
#     image_url = models.CharField(max_length=1080)
#     # image = models.ImageField(upload_to='products\imageFiles')


# class Offer(models.Model):
#     code = models.CharField(max_length=20)
#     description = models.CharField(max_length=50)
#     discount = models.FloatField()


class Category(MPTTModel):
    name = models.CharField(
        verbose_name=("Category Name"),
        help_text=("Unique"),
        max_length=255,
        unique=True,
    )

    slug = models.SlugField(
        verbose_name=("Category safe URL"),
        max_length=255,
        unique=True,
    )
    parent = TreeForeignKey(
        "self", on_delete=models.CASCADE, null=True, blank=True, related_name="children"
    )
    is_active = models.BooleanField(default=True)
    description = models.TextField(
        verbose_name=("description"), help_text=("not required"), blank=True
    )
    image = models.ImageField(
        verbose_name=("category image"),
        help_text=("upload the category image"),
        upload_to="images/category",
        default="images/category/default.png",
    )

    class MPTTMeta:
        order_insertion_by = ["name"]

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"

    def get_absolute_url(self):
        return reverse("store:category_list", args=[self.slug])

    def __str__(self):
        return self.name


class ProductType(models.Model):
    # different types of product that are for sale

    name = models.CharField(
        verbose_name=("Product Name"),
        help_text=("Required"),
        max_length=255,
        unique=True,
    )
    is_active = models.BooleanField(default=True)

    class Meta:
        verbose_name = "Product Type"
        verbose_name_plural = "Product Types"

    def __str__(self):
        return self.name


class ProductSpecification(models.Model):
    # features for the product types

    product_type = models.ForeignKey(ProductType, on_delete=models.RESTRICT)
    name = models.CharField(
        verbose_name=("Name"), help_text=("Required"), max_length=255, unique=True
    )

    class Meta:
        verbose_name = "ProductSpecification"
        verbose_name_plural = "ProductSpecifications"

    def __str__(self):
        return self.name


class Product(models.Model):
    # features for the product types

    product_type = models.ForeignKey(
        ProductType, related_name="categories", on_delete=models.RESTRICT
    )
    category = models.ForeignKey(
        Category, related_name="product_types", on_delete=models.RESTRICT
    )
    title = models.CharField(
        verbose_name=("Title"), help_text=("required"), max_length=255
    )
    description = models.TextField(
        verbose_name=("description"), help_text=("not required"), blank=True
    )
    slug = models.SlugField(max_length=255)
    regular_price = models.DecimalField(
        verbose_name=("Regular Price"),
        help_text=("Maximum 99,999"),
        error_messages={
            "name": {
                "max_length": ("THe price should be between 0 and 99,999"),
            },
        },
        max_digits=6,
        decimal_places=2,
    )
    discount_price = models.DecimalField(
        verbose_name=("Discount Price"),
        help_text=("Maximum 99,999"),
        error_messages={
            "name": {
                "max_length": ("The price should be between 0 and 99,999"),
            },
        },
        max_digits=6,
        decimal_places=2,
    )

    is_active = models.BooleanField(
        verbose_name=("Product visibility"),
        help_text=("Change product visibility"),
        default=True,
    )
    created_at = models.DateTimeField(("Created at"), auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(("Updated at"), auto_now=True)

    class Meta:
        ordering = ["-created_at"]
        verbose_name = "Product"
        verbose_name_plural = "Products"

    def __str__(self):
        return self.title

    def __str__(self):
        return self.title


class ProductSpecificationValue(models.Model):
    # holds each of the products individual specification/features

    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    specification = models.ForeignKey(ProductSpecification, on_delete=models.RESTRICT)

    value = models.CharField(
        verbose_name=("value"),
        help_text=("product specification value(maximum of 255 words)"),
        max_length=255,
    )

    class Meta:
        verbose_name = "Product specification value"
        verbose_name_plural = "Products specification values"

    def __str__(self):
        return self.value


class ProductImage(models.Model):
    # image table

    product = models.ForeignKey(
        Product, on_delete=models.CASCADE, related_name="product_image"
    )

    image = models.ImageField(
        verbose_name=("images"),
        help_text=("upload the product image"),
        upload_to="images",
        default="images/default.png",
    )
    alt_text = models.CharField(
        verbose_name=("Alternative Text"),
        help_text=("Please add alternative text"),
        max_length=255,
        null=True,
        blank=True,
    )
    is_feature = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    UPDATED_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "product Image"
        verbose_name_plural = "product Images"


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField()
    email = models.EmailField()

    def __str__(self):
        return self.user
