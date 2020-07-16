from django.db import models

# Create your models here.

class Cliente(models.Model):
    NIT = models.CharField(max_length=50)
    name = models.CharField(max_length=100)
    phone = models.IntegerField()
    adress = models.CharField(max_length=100)
