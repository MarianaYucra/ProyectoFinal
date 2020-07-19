from django.shortcuts import render

# Create your views here.

from .models import Producto
from .models import Categoria

def indexProducto(request):
    return render(request,"indexProducto.html")

def listarProducto(request):
    obj = Producto.objects.all()
    context = {
        'objeto' : obj,
    }
    return render(request, "listarProducto.html", context)

def listarCategoria(request):
    obj = Categoria.objects.all()
    context = {
        'objeto' : obj,
    }
    return render(request, "listarCategoria.html", context)


