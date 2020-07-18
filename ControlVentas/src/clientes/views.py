from django.shortcuts import render,redirect
from .models import Cliente
from .forms import ClienteForm
from django.views.generic import (
        ListView,
        DetailView,
        CreateView,
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

class ClientListView(ListView):
    model = Cliente
    template_name = 'showListClient.html'

class ShowClient(DetailView):
    model = Cliente
    template_name = 'showClient.html'
