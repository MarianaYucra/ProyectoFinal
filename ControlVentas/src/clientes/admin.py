from django.contrib import admin
from .models import Cliente, Contact, Proveedor

# Register your models here.
admin.site.register(Cliente)
admin.site.register(Contact)
admin.site.register(Proveedor)
