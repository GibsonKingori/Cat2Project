# store/models.py

from django.db import models

class Customer(models.Model):
    """
    Represents a customer in the e-commerce application.
    Each customer can place multiple orders.
    """
    name = models.CharField(max_length=255)  # Customer's name
    email = models.EmailField(unique=True)    # Customer's email (must be unique)

    def __str__(self):
        return self.name

class Order(models.Model):
    """
    Represents an order placed by a customer.
    Each order is associated with only one customer.
    """
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name='orders')
    order_date = models.DateTimeField(auto_now_add=True)  # Timestamp when the order was created
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)  # Total amount for the order

    def __str__(self):
        return f"Order {self.id} by {self.customer.name}"