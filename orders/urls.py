
from rest_framework.routers import SimpleRouter

from .views import OrderViewSet, OrderDetailViewSet


router = SimpleRouter()
router.register(r"v1/orders", OrderViewSet, basename="Order")
router.register(r"v1/order-detail", OrderDetailViewSet, basename="OrderDetail")

urlpatterns = router.urls
