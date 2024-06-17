# order.py
from django.db import models
from .customer import Customer

class Order(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Pendiente'),
        ('preparing', 'Preparando'),
        ('completed', 'Completado'),
    ]

    customer = models.ForeignKey(Customer, related_name='orders', on_delete=models.CASCADE, default=1)  # Supongamos que el ID del primer cliente es 1
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='pending')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'Order {self.id} by {self.customer.name}'
