from django.db import models

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=50)
    price = models.FloatField()
    stock = models.IntegerField()
    image_url = models.CharField(max_length=1080)


class Offer(models.Model):
    code = models.CharField(max_length=20)
    description = models.CharField(max_length=50)
    discount = models.FloatField()

