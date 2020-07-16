from django.urls import path
from . import views

urlpatterns = [
    path('añadirC/',views.newClient, name="nuevoCliente"),

]

