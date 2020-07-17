from django.shortcuts import render,redirect
from .models import Cliente
from django.urls import reverse_lazy
from django.views.generic import (
        ListView,
        DetailView,
        CreateView,
        DeleteView,
        UpdateView,
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
        ]
    success_url = reverse_lazy('cliente-list')

