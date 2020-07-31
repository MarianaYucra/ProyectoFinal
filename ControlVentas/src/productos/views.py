from django.shortcuts import render

# Create your views here.

from .models import Producto
from .models import Categoria
from django.views.generic import (ListView, DetailView, DeleteView, UpdateView, CreateView,)

from django.urls import reverse_lazy

class ProductoUpdateView(UpdateView):
    model = Producto
    fields = [
            'nombre',
            'codigo',
            'costo',
            'categoria',
            'marca',
            'img',
            'offer',
            'activado',
    ]
class ProductoDeleteView(DeleteView):
    model = Producto
    success_url = reverse_lazy('productos:producto-list')

class ProductoListView(ListView):
    model = Producto

class ProductoDetailView(DetailView):
    model = Producto

class ProductoCreateView(CreateView):
    model = Producto
    fields = [
            'nombre',
            'codigo',
            'costo',
            'categoria',
            'marca',   
            'img',
            'offer'.
            'activado',
    ]
class CategoriaUpdateView(UpdateView):
    model = Categoria
    fields = [
            'nombre',
            'activado',
            'img'
    ]
class CategoriaDeleteView(DeleteView):
    model = Categoria
    success_url = reverse_lazy('productos:producto-list')

class CategoriaListView(ListView):
    model = Categoria

class CategoriaDetailView(DetailView):
    model = Categoria

class CategoriaCreateView(CreateView):
    model = Categoria
    fields = [
            'nombre',
            'activado',
            'img',
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


