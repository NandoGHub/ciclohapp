
from rest_framework.routers import SimpleRouter

from .views import ProductViewSet


router = SimpleRouter()
router.register(r"v1/products", ProductViewSet, basename="Product")

urlpatterns = router.urls
