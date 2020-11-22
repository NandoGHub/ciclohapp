
import uuid
from django.db import models


class Product(models.Model):

    uuid = models.UUIDField(
        "UUID", default=uuid.uuid4, editable=False, unique=True,
        primary_key=True
    )
    name = models.CharField(max_length=100, null=True, blank=True)
    price = models.FloatField(null=True, blank=True)
    stock = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return f"{self.name} | {self.price} | {self.stock}"
