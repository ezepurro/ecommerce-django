from django.contrib import admin
from .models import Product

# Register your models here.

class ServiceAdmin(admin.ModelAdmin):
    pass

admin.site.register(Product, ServiceAdmin)