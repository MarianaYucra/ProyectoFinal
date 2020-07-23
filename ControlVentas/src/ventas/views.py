from django.shortcuts import render
from .models import Venta
from django.views.generic import (ListView, UpdateView, DetailView,)



# Create your views here.
def index (request):
    return render(request,"index.html")


class VentaListView(ListView):
    model = Venta

    
class VentaUpdateView(UpdateView):
    model = Venta
    fiels = [
        'codigo',
        'cliente',
        'producto',
        'cantidad',
        'precioU',
        'precioV',
        'pago',
        'fecha',

    ]
class VentaDetailView(DetailView):
    model = Venta

#def listar(request):
#    obj = Venta.objects.all()
#    context = {
#        'objeto' : obj,
#    }
#    return render(request, "listar.html", context)
