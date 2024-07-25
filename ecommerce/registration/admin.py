from django.contrib import admin
from .models import Seller

# Register your models here.

class ServiceAdmin(admin.ModelAdmin):
    list_display = ['user', 'phone_number', 'direction', 'avatar']

admin.site.register(Seller, ServiceAdmin)