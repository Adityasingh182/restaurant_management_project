from django.db import models
from .models import OrderStatus
# Create your models here.
class order (models.Model):
    status = models.foreignKey(
        OrderStatus,
        on_delete=models.SET_NULL,
        null=true
    )