from django.shortcuts import render

# Create your views here.

from .models import Producto
from .models import Categoria
from django.views.generic import (ListView, CreateView,)



class ProductoListView(ListView):
    model = Producto

#class ProductoDetailView(DetailView):
    #model = Producto

class ProductoCreateView(CreateView):
    model = Producto
    fields = [
            'nombre',
            'codigo',
            'costo',
            'categoria',
            'marca',
            
    ]

#def indexProducto(request):
    #return render(request,"indexProducto.html")

#def listarProducto(request):
 #   obj = Producto.objects.all()
  #  context = {
   #     'objeto' : obj,
    #}
    #return render(request, "listarProducto.html", context)

#def listarCategoria(request):
 #   obj = Categoria.objects.all()
  #  context = {
   #     'objeto' : obj,
   # }
   # return render(request, "listarCategoria.html", context)


