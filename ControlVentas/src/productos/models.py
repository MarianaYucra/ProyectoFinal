from django.db import models
from django.urls import reverse
# Create your models here.


class Categoria(models.Model):
    nombre = models.CharField(max_length = 10)
    activado = models.BooleanField(default = True)

    def get_absolute_url(self):
        return reverse('productos:categoria-detail', kwargs = {'pk': self.id})


class Producto(models.Model):
    nombre = models.CharField(max_length = 10)
    codigo = models.CharField(max_length = 10)
    costo = models.DecimalField(max_digits = 9, decimal_places = 2)
    categoria = models.CharField(max_length = 10,)
    marca = models.CharField(max_length = 10)

    def get_absolute_url(self):
        return reverse('productos:producto-detail', kwargs = {'pk': self.id})

