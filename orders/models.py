from django.db import models
from .models import OrderStatus
# Create your models here.
class order (models.Model):
    status = models.foreignKey(
        OrderStatus,
        on_delete=models.SET_NULL,
        null=true
    )

class OrderStatus(models.Model):
    name = models.CharField(max_length=50,unique=True)
    
    def __str__(self):
        return self.name

class Coupon(models.Model):
    code = models.CharField(max_length=50, unique=true)
    discount_percentage = models.DecimalsField(max_digits=5, decimal_places=2)
    is_active = models,BooleanField(default=True)
    valid_from = models.DataField()
    valid_until = models.DataField()

    def __str__(self):
        return self.name