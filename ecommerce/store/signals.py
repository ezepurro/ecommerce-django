from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver
from .models import Product


# @receiver(post_save, sender=Product)
# def my_callback(sender, instance, created, **kwargs):
#     import inspect
#     for frame_record in inspect.stack():
#         if frame_record[3]=='get_response':
#             request = frame_record[0].f_locals['request']
#             break
#     else:
#         request = None

#     if created:
#         instance.seller = request.user
#         instance.save()