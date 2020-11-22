from django.db.models.signals import post_save, pre_delete
from django.dispatch import receiver

from .models import OrderDetail


@receiver(post_save, sender=OrderDetail)
def product_stock_discount(sender, instance, created, **kwargs):
    product = instance.product
    product.stock = product.stock - instance.cuantity
    product.save()


@receiver(pre_delete, sender=OrderDetail)
def product_stock_restore(sender, instance, **kwargs):
    product = instance.product
    product.stock = product.stock + instance.cuantity
    product.save()
