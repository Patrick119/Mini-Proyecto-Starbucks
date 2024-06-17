# forms.py
from django import forms
from .customer import Customer
from .order import Order
from .order_item import OrderItem

class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ['name', 'email', 'phone_number', 'address']

class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['status', 'total_price']

class OrderItemForm(forms.ModelForm):
    class Meta:
        model = OrderItem
        fields = ['product', 'quantity', 'price']
