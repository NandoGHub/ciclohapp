from django.contrib import admin
from .models import Product


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_fields = [
        'uuid',
        'name',
        'price',
        'stock'
    ]
    search_fields = ('uuid', 'name')