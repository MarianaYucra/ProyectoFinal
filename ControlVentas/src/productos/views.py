from django.shortcuts import render
from .models import Producto
from .models import Categoria
from django.urls import reverse_lazy
from django.views.generic import (ListView, DetailView, DeleteView, UpdateView, CreateView,)

from django.http import HttpResponse
from django.views.generic import View
from django.template.loader import get_template
from .utils import render_to_pdf #created in step 4



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
            'img',
            'offer',
            'activado',
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
            'img',
            'offer',
            'activado',
    ]
class CategoriaUpdateView(UpdateView):
    model = Categoria
    template_name = 'updateObject.html'
    fields = [
            'nombre',
            'activado',
            'img'
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
            'img',
    ]


class GeneratePDF(View):
    def get(self, request, *args, **kwargs):
        template = get_template('pdf/pdfProductos.html')
        obj  = Producto.objects.all()
        context = {
            'obj':obj,
        }   
        html = template.render(context)
        pdf = render_to_pdf('pdf/pdfProductos.html', context)
        if pdf:
            response = HttpResponse(pdf, content_type='application/pdf')
            filename = "Invoice_%s.pdf" %("12341231")
            content = "inline; filename='%s'" %(filename)
            download = request.GET.get("download")
            if download:
                content = "attachment; filename='%s'" %(filename)
            response['Content-Disposition'] = content
            return response
        return HttpResponse("Not found")


class GeneratePDFCategoria(View):
    def get(self, request, *args, **kwargs):
        template = get_template('pdf/pdfCategorias.html')
        obj  = Categoria.objects.all()
        context = {
            'obj':obj,
        }
        html = template.render(context)
        pdf = render_to_pdf('pdf/pdfCategorias.html', context)
        if pdf:
            response = HttpResponse(pdf, content_type='application/pdf')
            filename = "Invoice_%s.pdf" %("12341231")
            content = "inline; filename='%s'" %(filename)
            download = request.GET.get("download")
            if download:
                content = "attachment; filename='%s'" %(filename)
            response['Content-Disposition'] = content
            return response
        return HttpResponse("Not found")


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


