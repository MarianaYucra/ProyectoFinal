from django.db import models

# Create your models here.

TIPO_CHOICES = (
    ('contado', 'CONTADO'),
    ('partes', 'PARTES'),
)

class Venta(models.Model):
    codigo = models.CharField(max_length = 10)
    cliente = models.CharField(max_length = 100)
    producto = models.CharField(max_length = 100)
    cantidad = models.IntegerField()
    precioU = models.DecimalField(max_digits = 9, decimal_places = 2)
    precioV = models.DecimalField(max_digits = 9, decimal_places = 2)
    pago = models.CharField(max_length = 10, choices = TIPO_CHOICES, default = 'contado')
    fecha = models.DateField()
