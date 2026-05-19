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