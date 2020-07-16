from django import forms
from .models import Venta

class VentaForm(forms.ModelForm):
    class Meta:
        model = Destination
        fields = [
                'codigo',
                'cliente',
                'producto',
                'cantidad',
                'precioU',
                'precioV',
                'pago',
                'fecha',
                ]
