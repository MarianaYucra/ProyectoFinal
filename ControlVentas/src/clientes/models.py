from django.db import models
from django.urls import reverse

# Create your models here.


GENDER_CHOICES = (
    ('male', 'MASCULINO'),
    ('female', 'FEMENINO'),
)

STATE_CHOICES = (
    ('active', 'ACTIVO'),
    ('inactive', 'INACTIVO'),
)

class Cliente(models.Model):
    NIT = models.CharField(max_length=50)
    name = models.CharField(max_length=100)
    phone = models.IntegerField()
    adress = models.CharField(max_length=100)
    NRC = models.CharField(max_length=100)
    gender = models.CharField(max_length = 10, choices = GENDER_CHOICES, default = 'contado')
    state = models.CharField(max_length = 10, choices = STATE_CHOICES, default = 'contado')
    date = models.DateTimeField(auto_now_add=True)

    def get_absolute_url(self):
        return reverse('cliente-detail', kwargs= {'pk':self.id})

DEGREE_CHOICES = (
    ('primary', 'PRINCIPAL'),
    ('secondary', 'SEGUNDARIO'),
    ('tertiary', 'TERCIARIO'),
)

class Contact(models.Model):   
    name = models.CharField(max_length=100, verbose_name="Nombre Contacto")
    email = models.EmailField(max_length=100, verbose_name="Correo")
    phone = models.IntegerField(null=True, verbose_name="Telefono")
    cellPhone = models.IntegerField(verbose_name="Celular")
    degree = models.CharField(max_length = 10, choices = DEGREE_CHOICES, default = 'primary', verbose_name="Nivel Contacto")
    date = models.DateTimeField(auto_now_add=True)

STATE_CHOICES = (
    ('active', 'ACTIVO'),
    ('inactive', 'INACTIVO'),
)

class Proveedor(models.Model): 
    name = models.CharField(max_length=100, verbose_name="Nombre Empresa Proveedora")
    adress = models.CharField(max_length=100, verbose_name="Direccion")
    contact = models.ForeignKey(Contact, on_delete=models.SET_NULL, null=True)
    NIT = models.CharField(max_length=50)
    phone = models.IntegerField(verbose_name="Telefono Empresa")
    FAX = models.CharField(max_length=50)
    state = models.CharField(max_length = 10, choices = STATE_CHOICES, default = 'active', verbose_name="Estado")
    date = models.DateTimeField(auto_now_add=True)

