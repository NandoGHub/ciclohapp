from django.apps import AppConfig


class OrdersConfig(AppConfig):
    name = 'orders'
    label = 'orders'
    verbose_name = "Cicloh Apps Orders"

    def ready(self):
        from .signals import product_stock_discount, product_stock_restore
