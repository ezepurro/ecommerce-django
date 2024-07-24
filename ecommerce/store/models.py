from django.db import models

# Create your models here.

class Product(models.Model):
    title = models.CharField(max_length=200, verbose_name="Title")
    description = models.TextField(verbose_name="Description")
    price = models.CharField(max_length=6, verbose_name="Price")
    image = models.ImageField(verbose_name="Image", upload_to="store")
    published = models.DateTimeField(auto_now_add=True, verbose_name="Publish date")

    class Meta:
             verbose_name = "Product"
             verbose_name_plural = "Products"
             ordering = ['-published']

    def __str__(self):
             return self.title