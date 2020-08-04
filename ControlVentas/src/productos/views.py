from django.shortcuts import render
from .models import Producto
from .models import Categoria
from django.urls import reverse_lazy
from django.views.generic import (ListView, DetailView, DeleteView, UpdateView, CreateView,)

# Create your views here.

class ProductoUpdateView(UpdateView):
    model = Producto
    template_name = 'updateObject.html'
    fields = [
            'nombre',
            'codigo',
            'costo',
            'categoria',
            'marca',
            'estado',
    ]
class ProductoDeleteView(DeleteView):
    model = Producto
    template_name = 'deleteObject.html'
    success_url = reverse_lazy('productos:producto-list')

class ProductoListView(ListView):
    model = Producto

class ProductoDetailView(DetailView):
    model = Producto

class ProductoCreateView(CreateView):
    model = Producto
    template_name = 'createObject.html'
    fields = [
            'nombre',
            'codigo',
            'costo',
            'categoria',
            'marca', 
            'estado',         
    ]
class CategoriaUpdateView(UpdateView):
    model = Categoria
    template_name = 'updateObject.html'
    fields = [
            'nombre',
            'activado',
    ]
class CategoriaDeleteView(DeleteView):
    model = Categoria
    template_name = 'deleteObject.html'
    success_url = reverse_lazy('productos:producto-list')

class CategoriaListView(ListView):
    model = Categoria

class CategoriaDetailView(DetailView):
    model = Categoria

class CategoriaCreateView(CreateView):
    model = Categoria
    template_name = 'createObject.html'
    fields = [
            'nombre',
            'activado',
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


