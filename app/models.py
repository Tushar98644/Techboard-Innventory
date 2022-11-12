from django.db import models

# Create your models here.
class Inventory(models.Model):
    product = models.CharField(max_length=100)
    price = models.IntegerField()
    Quantity = models.IntegerField()
