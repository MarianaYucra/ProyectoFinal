from django.shortcuts import render,redirect
from .models import Cliente
from .forms import ClienteForm


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
