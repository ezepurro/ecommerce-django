from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Seller(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=30, null=True, blank=True, verbose_name='Phone number')
    direction = models.CharField(max_length=80, null=True, blank=True, verbose_name='Direction')
    avatar = models.ImageField(upload_to='members', null=True, blank=True, verbose_name='Avatar')

    class Meta:
        verbose_name = "Seller"
        verbose_name_plural = "Sellers"
        ordering = ['-user']

    def __str__(self):
        return self.user.username