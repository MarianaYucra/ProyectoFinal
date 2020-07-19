from django.db import models

# Create your models here.


class Producto(models.Model):
    nombre = models.CharField(max_length = 10)
    codigo = models.CharField(max_length = 10)
    costo = models.DecimalField(max_digits = 9, decimal_places = 2) 
    categoria = models.CharField(max_length = 10)
    marca = models.CharField(max_length = 10)


class Categoria(models.Model):
    nombre = models.CharField(max_length = 10)
    activado = models.BooleanField(default = True)

