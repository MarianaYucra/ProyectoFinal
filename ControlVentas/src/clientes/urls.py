from django.urls import path
from . import views

urlpatterns = [
    path('listaC/',views.showListClient, name="listaCliente"),
    path('añadirC/',views.newClient, name="nuevoCliente"),

]

