from django.shortcuts import render,redirect
from .models import Venta
from django.views.generic import (ListView, UpdateView, DetailView,)



# Create your views here.
def index (request):
    return render(request,"index.html")

def administration (request):
    return render(request,"administration.html")

def newRecord(request):
    if request.method == 'POST':
        codigo = request.POST['codigo']
        cliente = request.POST['cliente']
        producto = request.POST['producto']
        cantidad = request.POST['cantidad']
        precioU = request.POST['precioU']
        precioV = request.POST['precioV']
        pago = request.POST['pago']
        fecha = request.POST['fecha']

        ventaR = Venta.objects.create(codigo=codigo, cliente=cliente, producto=producto,cantidad=cantidad,precioU=precioU, precioV=precioV, pago=pago, fecha=fecha)
        ventaR.save()
        return redirect('/')

    else:
        return render(request,'newRecord.html')

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
