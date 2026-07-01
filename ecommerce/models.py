from django.db import models
from helpers.models import TrackingModel, BasicModel
from helpers.functions import random_image, random_decimal
from accounts.models import User
# Create your models here.

class Category(TrackingModel, BasicModel):
    def __str__(self):
        return self.name

class Product(TrackingModel, BasicModel):
    # Item price
    price = models.DecimalField(verbose_name="Item value", blank=True, null=True, decimal_places=2, max_digits=9, default=random_decimal)
    # Item image
    image = models.ImageField(verbose_name="Image", null=True, blank=True, upload_to='', default=random_image)
    # Item categories
    categories = models.ManyToManyField(Category, verbose_name="Categories", related_name='products', blank=True)
    # Stock item
    stock = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.name

class CartItem(models.Model):
    # related_name debe ser un identificador válido (sin espacios)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='items')
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

class CollectionItem(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='collection')
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)