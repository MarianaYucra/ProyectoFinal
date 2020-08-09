from django.shortcuts import render,redirect
from .models import Cliente, Contact, Proveedor
from django.urls import reverse_lazy
from django.views.generic import ( ListView, DetailView, CreateView, DeleteView, UpdateView,
    )


from django.http import HttpResponse
from django.views.generic import View
from django.template.loader import get_template
from .utils import render_to_pdf #created in step 4


# Create your views here.

def newClient(request):
    form = ClienteForm()
    if request.method == "POST":
        form = ClienteForm(request.POST or None)
        if form.is_valid():
            form.save()
            form = ClienteForm()
            return redirect('/')

    context = {
            'form': form
            }

    return render(request,'insertClient.html', context)


def showListClient (request):
    queryset = Cliente.objects.all()
    context = {
            'objectList':queryset,
            }

    return render(request, 'showListClient.html', context)

class ClientCreateView(CreateView):
    model = Cliente
    template_name = 'createObject.html'
    fields = [
            'NIT',
            'name',
            'phone',
            'adress',
            'NRC',
            'gender',
            'state',
        ]
    success_url = reverse_lazy('clientes:cliente-list')

class ClientDeleteView(DeleteView):
    model = Cliente
    template_name = 'deleteObject.html'
    success_url = reverse_lazy('clientes:cliente-list')

class ClientListView(ListView):
    model = Cliente
    template_name = 'showListClient.html'

class ShowClient(DetailView):
    model = Cliente
    template_name = 'showClient.html'

class ClientUpdateView(UpdateView):
    model = Cliente
    template_name = 'updateObject.html'
    fields = [
            'NIT',
            'name',
            'phone',
            'adress',
            'NRC',
            'gender',
            'state',
        ]
    success_url = reverse_lazy('clientes:cliente-list')

#***************************PROVEEDOR*****************************************

class ProveedorListView(ListView):
    model = Proveedor
    template_name = 'showListProveedor.html'


class ProveedorCreateView(CreateView):
    model = Proveedor
    template_name = 'createObject.html'
    fields = [
            'name',
            'adress',
            'contact',
            'NIT',
            'phone',
            'FAX',
            'state',
        ]
    success_url = reverse_lazy('clientes:proveedor-list')

class ProveedorDeleteView(DeleteView):
    model = Proveedor
    template_name = 'deleteObject.html'
    success_url = reverse_lazy('clientes:proveedor-list')


class ProveedorDetailView(DetailView):
    model = Proveedor
    template_name = 'showProveedor.html'

class ProveedorUpdateView(UpdateView):
    model = Proveedor
    template_name = 'updateObject.html'
    fields = [
            'name',
            'adress',
            'contact',
            'NIT',
            'phone',
            'FAX',
            'state',
        ]
    success_url = reverse_lazy('clientes:proveedor-list')

#***************************Contact*****************************************

class ContactListView(ListView):
    model = Contact
    template_name = 'showListContact.html'


class ContactCreateView(CreateView):
    model = Contact
    template_name = 'createObject.html'
    fields = [
            'name',
            'email',
            'phone',
            'cellPhone',
            'degree',
        ]
    success_url = reverse_lazy('clientes:contacto-list')

class ContactDetailView(DetailView):
    model = Contact
    template_name = 'showContact.html'


class ContactDeleteView(DeleteView):
    model = Contact
    template_name = 'deleteObject.html'
    success_url = reverse_lazy('clientes:contacto-list')

class ContactUpdateView(UpdateView):
    model = Contact
    template_name = 'updateObject.html'
    fields = [
            'name',
            'email',
            'phone',
            'cellPhone',
            'degree',
        ]
    success_url = reverse_lazy('clientes:contacto-list')




class GeneratePDFCliente(View):
    def get(self, request, *args, **kwargs):
        template = get_template('pdf/pdfCliente.html')
        obj  = Cliente.objects.all()
        context = {
            'obj':obj,
        }
        html = template.render(context)
        pdf = render_to_pdf('pdf/pdfCliente.html', context)
        if pdf:
            response = HttpResponse(pdf, content_type='application/pdf')
            filename = "CLientee_%s.pdf" %("12341231")
            content = "inline; filename='%s'" %(filename)
            download = request.GET.get("download")
            if download:
                content = "attachment; filename='%s'" %(filename)
            response['Content-Disposition'] = content
            return response
        return HttpResponse("Not found")


class GeneratePDFContacto(View):
    def get(self, request, *args, **kwargs):
        template = get_template('pdf/pdfContacto.html')
        obj  = Contact.objects.all()
        context = {
            'obj':obj,
        }
        html = template.render(context)
        pdf = render_to_pdf('pdf/pdfContacto.html', context)
        if pdf:
            response = HttpResponse(pdf, content_type='application/pdf')
            filename = "Contacto_%s.pdf" %("12341231")
            content = "inline; filename='%s'" %(filename)
            download = request.GET.get("download")
            if download:
                content = "attachment; filename='%s'" %(filename)
            response['Content-Disposition'] = content
            return response
        return HttpResponse("Not found")

class GeneratePDFProveedor(View):
    def get(self, request, *args, **kwargs):
        template = get_template('pdf/pdfProveedor.html')
        obj  = Proveedor.objects.all()
        context = {
            'obj':obj,
        }
        html = template.render(context)
        pdf = render_to_pdf('pdf/pdfProveedor.html', context)
        if pdf:
            response = HttpResponse(pdf, content_type='application/pdf')
            filename = "Proveedor_%s.pdf" %("12341231")
            content = "inline; filename='%s'" %(filename)
            download = request.GET.get("download")
            if download:
                content = "attachment; filename='%s'" %(filename)
            response['Content-Disposition'] = content
            return response
        return HttpResponse("Not found")

