from django.db import models
from django.urls import reverse

# Create your models here.

class Cliente(models.Model):
    NIT = models.CharField(max_length=50)
    name = models.CharField(max_length=100)
    phone = models.IntegerField()
    adress = models.CharField(max_length=100)

    def get_absolute_url(self):
        return reverse('cliente-detail', kwargs= {'pk':self.id})
