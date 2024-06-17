from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from WebApp.StarbucksApp.views import CategoryViewSet, ProductViewSet, OrderViewSet, OrderItemViewSet, CustomerViewSet

router = DefaultRouter()
router.register(r'categories', CategoryViewSet)
router.register(r'products', ProductViewSet)
router.register(r'orders', OrderViewSet)
router.register(r'order-items', OrderItemViewSet)
router.register(r'customers', CustomerViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('admin/', admin.site.urls),
    path('api/', include('WebApp.StarbucksApp.urls')),  # Asegúrate de que este archivo exista
]
