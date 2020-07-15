from django.shortcuts import render
from .models import Venta

# Create your views here.
def index (request):
    return render(request,"index.html")

def listar(request):
    obj = Venta.objects.all()
    context = {
        'objeto' : obj,
    }
    return render(request, "listar.html", context)
