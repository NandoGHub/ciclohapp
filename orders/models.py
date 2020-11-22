
import uuid

from django.db import models
from django.utils import timezone

from orders.services.dollar_trading import DollarTradingService
from products.models import Product


class Order(models.Model):

    uuid = models.UUIDField(
        "UUID", default=uuid.uuid4, editable=False, unique=True,
        primary_key=True
    )
    date_time = models.DateTimeField(default=timezone.now)

    @property
    def get_total(self):
        return sum([
            item.product.price * item.cuantity
            for item in self.order_details.all()
        ])

    @property
    def get_total_usd(self):
        service = DollarTradingService()
        dollar = service.get()
        if dollar != 0:
            return round(self.get_total / dollar, 2)
        return 0

    def __str__(self):
        return f"{self.uuid} | {self.date_time}"


class OrderDetail(models.Model):

    uuid = models.UUIDField(
        "UUID", default=uuid.uuid4, editable=False, unique=True,
        primary_key=True
    )
    order = models.ForeignKey(
        Order,
        related_name="order_details",
        on_delete=models.CASCADE,
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
        return f"{self.order} | {self.cuantity} | {self.product}"
