from django.urls import path
from . import views
from .views import (
        ClientListView,
        ShowClient,
        ClientCreateView,
        )

urlpatterns = [
    path('listaC/',views.showListClient, name="listaCliente"),
    path('lista/',ClientListView.as_view(), name="cliente-list"),
    path('añadirC/',views.newClient, name="nuevoCliente"),
    path('createC/',ClientCreateView.as_view(), name="cliente-create"),
    path('<int:pk>/',ShowClient.as_view(), name="cliente-detail"),
]

