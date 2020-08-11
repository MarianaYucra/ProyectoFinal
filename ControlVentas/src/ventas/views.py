from django.shortcuts import render,redirect
from .models import Venta
from django.views.generic import (ListView, UpdateView, DetailView,)
from productos.models import Producto, Categoria



from django.http import HttpResponse
from django.views.generic import View
from django.template.loader import get_template
from .utils import render_to_pdf #created in step 4


# Create your views here.
def index (request):
    obj2 = Producto.objects.all() 
    obj  = Categoria.objects.all()
    context = {
        'obj':obj,
        'obj2':obj2,
    }
    return render(request,"index.html", context)

def administration (request):
    return render(request,"examples/administration.html")

def newRecord(request):


    template_name = 'createObject.html'
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
        return render(request,'createObject.html')


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







class GeneratePDFVenta(View):
    def get(self, request, *args, **kwargs):
        template = get_template('pdf/pdfVenta.html')
        obj  = Venta.objects.all()
        context = {
            'obj':obj,
        }
        html = template.render(context)
        pdf = render_to_pdf('pdf/pdfVenta.html', context)
        if pdf:
            response = HttpResponse(pdf, content_type='application/pdf')
            filename = "VEnta_%s.pdf" %("12341231")
            content = "inline; filename='%s'" %(filename)
            download = request.GET.get("download")
            if download:
                content = "attachment; filename='%s'" %(filename)
            response['Content-Disposition'] = content
            return response
        return HttpResponse("Not found")

#def listar(request):
#    obj = Venta.objects.all()
#    context = {
#        'objeto' : obj,
#    }
#    return render(request, "listar.html", context)

