from django.db import models
from django.contrib.auth.models import User
from registration.models import Seller

# Create your models here.

STATUS_CHOICES = (
       ('New', 'New'),
       ('Used as new', 'Used as new'),
       ('Used', 'Used'),
       ('Refurbished', 'Refurbished'),
)


class Product(models.Model):
    title = models.CharField(max_length=200, verbose_name="Title")
    description = models.TextField(verbose_name="Description")
    price = models.CharField(max_length=6, verbose_name="Price")
    image = models.ImageField(verbose_name="Image", upload_to="store")
    seller = models.ForeignKey(Seller, verbose_name="Seller", on_delete=models.CASCADE, related_name='%(class)s_seller', null=True, blank=True)
    state = models.CharField(max_length=20, choices=STATUS_CHOICES, default='Used')
    published = models.DateTimeField(auto_now_add=True, verbose_name="Publish date")

    class Meta:
             verbose_name = "Product"
             verbose_name_plural = "Products"
             ordering = ['-published']

    def __str__(self):
             return self.title