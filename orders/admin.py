from django.contrib import admin
from .models import Order, OrderDetail


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_fields = [
        'uuid',
        'date_time'
    ]
    search_fields = ('uuid',)


@admin.register(OrderDetail)
class OrderDetailAdmin(admin.ModelAdmin):
    list_fields = [
        'uuid',
        'order',
        'cuantity',
        'product'
    ]
    search_fields = ('uuid', 'order__uuid', 'product__uuid')
