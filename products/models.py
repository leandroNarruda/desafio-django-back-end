from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=255)
    code = models.CharField(max_length=255)
    category = models.CharField(max_length=255)
    provider = models.CharField(max_length=255)
    amount = models.DecimalField(max_digits=8, decimal_places=2)
