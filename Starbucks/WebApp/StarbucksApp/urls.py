from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CategoryViewSet, ProductViewSet, OrderViewSet, OrderItemViewSet, CustomerViewSet

router = DefaultRouter()
router.register(r'categories', CategoryViewSet)
router.register(r'products', ProductViewSet)
router.register(r'orders', OrderViewSet)
router.register(r'order-items', OrderItemViewSet)
router.register(r'customers', CustomerViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
