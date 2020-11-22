
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from .models import Order, OrderDetail
from .serializers import OrderSerializer, OrderDetailSerializer


class OrderViewSet(viewsets.ModelViewSet):
    serializer_class = OrderSerializer
    queryset = Order.objects.all()
    permission_classes = [IsAuthenticated]
    http_method_names = ('get', 'post', 'put', 'patch', 'delete')
    lookup_field = 'uuid'


class OrderDetailViewSet(viewsets.ModelViewSet):
    serializer_class = OrderDetailSerializer
    queryset = OrderDetail.objects.all()
    permission_classes = [IsAuthenticated]
    http_method_names = ('get', 'post', 'put', 'patch', 'delete')
    lookup_field = 'uuid'
