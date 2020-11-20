
import uuid
from django.db import models
from products.models import Product


class Order(models.Model):

    uuid = models.UUIDField(
        "UUID", default=uuid.uuid4, editable=False, unique=True
    )
    date_time = models.DateTimeField(auto_now_add=True, editable=False)

    def __str__(self):
        return f"{self.uuid}"


class OrderDetail(models.Model):

    uuid = models.UUIDField(
        "UUID", default=uuid.uuid4, editable=False, unique=True
    )
    order = models.ForeignKey(
        Order,
        related_name="order_details",
        on_delete=models.DO_NOTHING,
        null=True,
        blank=True
    )
    cuantity = models.IntegerField(null=True, blank=True)
    product = models.ForeignKey(
        Product,
        related_name="product_order_details",
        on_delete=models.DO_NOTHING,
        null=True,
        blank=True
    )

    def __str__(self):
        return f"{self.order} | {self.cuantity} {self.product}"