from django.contrib import admin
from .models import Order, OrderDetail


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = [
        'uuid',
        'date_time'
    ]
    search_fields = ('uuid',)


@admin.register(OrderDetail)
class OrderDetailAdmin(admin.ModelAdmin):
    list_display = [
        'uuid',
        'order',
        'cuantity',
        'product'
    ]
    search_fields = ('uuid', 'order__uuid', 'product__uuid')
