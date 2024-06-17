from django.contrib import admin
from .models.customer import Customer
from .models.category import Category
from .models.product import Product
from .models.order import Order
from .models.order_item import OrderItem

admin.site.register(Customer)
admin.site.register(Category)
admin.site.register(Product)
admin.site.register(Order)
admin.site.register(OrderItem)