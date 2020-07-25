from django.shortcuts import render,redirect
from .models import Cliente, Contact, Proveedor
from django.urls import reverse_lazy
from django.views.generic import ( ListView, DetailView, CreateView, DeleteView, UpdateView,
    )

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
    template_name = 'insertClient.html'
    fields = [
            'NIT',
            'name',
            'phone',
            'adress',
            'NRC',
            'gender',
            'state',
        ]
    success_url = reverse_lazy('cliente-list')

class ClientDeleteView(DeleteView):
    model = Cliente
    template_name = 'deleteClient.html'
    success_url = reverse_lazy('cliente-list')

class ClientListView(ListView):
    model = Cliente
    template_name = 'showListClient.html'

class ShowClient(DetailView):
    model = Cliente
    template_name = 'showClient.html'

class ClientUpdateView(UpdateView):
    model = Cliente
    template_name = 'insertClient.html'
    fields = [
            'NIT',
            'name',
            'phone',
            'adress',
            'NRC',
            'gender',
            'state',
        ]
    success_url = reverse_lazy('cliente-list')

#***************************PROVEEDOR*****************************************

class ProveedorListView(ListView):
    model = Proveedor
    template_name = 'showListProveedor.html'


class ProveedorCreateView(CreateView):
    model = Proveedor
    template_name = 'insertClient.html'
    fields = [
            'name',
            'adress',
            'contact',
            'NIT',
            'phone',
            'FAX',
            'state',
        ]
    success_url = reverse_lazy('Proveedor-list')

class ProveedorDeleteView(DeleteView):
    model = Proveedor
    template_name = 'deleteClient.html'
    success_url = reverse_lazy('proveedor-list')


class ProveedorDetailView(DetailView):
    model = Proveedor
    template_name = 'showProveedor.html'

class ProveedorUpdateView(UpdateView):
    model = Proveedor
    template_name = 'insertClient.html'
    fields = [
            'name',
            'adress',
            'contact',
            'NIT',
            'phone',
            'FAX',
            'state',
        ]
    success_url = reverse_lazy('Proveedor-list')

#***************************Contact*****************************************

class ContactListView(ListView):
    model = Proveedor
    template_name = 'showListContact.html'


class ContactCreateView(CreateView):
    model = Contact
    template_name = 'insertClient.html'
    fields = [
            'name',
            'email',
            'phone',
            'cellPhone',
            'degree',
        ]
    success_url = reverse_lazy('Proveedor-list')

class ContactDetailView(DetailView):
    model = Contact
    template_name = 'showContact.html'


class ContactDeleteView(DeleteView):
    model = Contact
    template_name = 'deleteClient.html'
    success_url = reverse_lazy('proveedor-list')

class ContactUpdateView(UpdateView):
    model = Contact
    template_name = 'insertClient.html'
    fields = [
            'name',
            'email',
            'phone',
            'cellPhone',
            'degree',
        ]
    success_url = reverse_lazy('Proveedor-list')
