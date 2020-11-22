from rest_framework import serializers

from .models import Order, OrderDetail
from products.models import Product
from products.serializers import ProductSerializer


class OrderSmallSerializer(serializers.ModelSerializer):

    class Meta:
        model = Order
        fields = "__all__"


class OrderDetailSerializer(serializers.ModelSerializer):

    order = OrderSmallSerializer(many=False)
    product = ProductSerializer(many=False)

    def validate_cuantity(self, value):
        if value < 1:
            raise serializers.ValidationError(
                "La cantidad debe ser mayor que cero")
        return value

    def validate_product(self, value):
        if value.stock < 1:
            raise serializers.ValidationError(
                "El producto no tiene stock disponible")
        return value

    class Meta:
        model = OrderDetail
        fields = ('uuid', 'order', 'cuantity', 'product')
        extra_kwargs = {
            'order': {'allow_null': False, 'required': True},
            'cuantity': {'allow_null': False, 'required': True},
            'product': {'allow_null': False, 'required': True}
        }


class OrderSerializer(serializers.ModelSerializer):
    order_details = OrderDetailSerializer(many=True, read_only=True)
    total = serializers.SerializerMethodField()
    total_usd = serializers.SerializerMethodField()

    def validate_order_details(self, value):
        if len(value) < 1 or value is None:
            raise serializers.ValidationError(
                "Order_details no puede estar vacío")
        return value

    def create(self, validated_data):
        order = Order()
        details = self.initial_data.get('order_details')
        all_right, message = self._validated_info(details)
        if not all_right:
            raise serializers.ValidationError({"error": message})
        order.save()
        for detail in details:
            data = {
                "cuantity": detail.get('cuantity'),
                "product": Product.objects.get(uuid=detail.get('product'))
            }
            OrderDetail.objects.create(order=order, **data)
        return order

    def update(self, instance, validated_data):
        order = instance
        details = self.initial_data.get('order_details')
        all_right, message = self._validated_info(details)
        if not all_right:
            raise serializers.ValidationError({"error": message})
        order.save()
        order.order_details.all().delete()
        for detail in details:
            data = {
                "cuantity": detail.get('cuantity'),
                "product": Product.objects.get(uuid=detail.get('product'))
            }
            OrderDetail.objects.create(order=order, **data)
        return order

    def _validated_info(self, payload):
        # VALIDA PRODUCTO REPETIDO
        check_products = self._repeat_products(payload)
        if check_products:
            return False, "No puede haber productos repetidos"
        # VALIDA CANTIDAD DE PRODUCTO MAYOR A CERO
        check_cuantity = self._cuantity_zero(payload)
        if check_cuantity:
            return False, "La cantidad debe ser mayor que cero"
        return True, ""

    @staticmethod
    def _repeat_products(payload):
        products_ids = [item["product"] for item in payload]
        return not len(products_ids) == len(set(products_ids))

    @staticmethod
    def _cuantity_zero(payload):
        return len(
            [item["cuantity"] for item in payload if item["cuantity"] < 1]
        ) > 0

    def get_total(self, instance):
        return instance.get_total

    def get_total_usd(self, instance):
        return instance.get_total_usd

    class Meta:
        model = Order
        fields = ('uuid', 'date_time', 'order_details', 'total', 'total_usd')
