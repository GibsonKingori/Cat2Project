from django.db import models

# Create your models here.
# Customer model
class Customer(models.Model):
    name = models.CharField(max_length=100)  # Customer's full name
    email = models.EmailField(unique=True)  # Ensure each email is unique

    def __str__(self):
        return self.name

# Order model
class Order(models.Model):
    customer = models.ForeignKey(
        Customer,
        on_delete=models.CASCADE,
        related_name='orders'
    )  # ForeignKey links each order to one customer
    order_date = models.DateTimeField(auto_now_add=True)  # Auto-set order date
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)  # Total order amount

    def __str__(self):
        return f"Order {self.id} - {self.customer.name}"
