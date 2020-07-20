from django.urls import path
from . import views
from .views import (
        ClientListView,
        ShowClient,
        ClientCreateView,
        ClientDeleteView,
        ClientUpdateView,
        ProveedorListView,
        ProveedorCreateView,
        )

urlpatterns = [
    path('lista/',views.showListClient, name="listaCliente"),
    path('añadir/',views.newClient, name="nuevoCliente"),
    path('list/',ClientListView.as_view(), name="cliente-list"),
    path('create/',ClientCreateView.as_view(), name="cliente-create"),
    path('<int:pk>/delete/',ClientDeleteView.as_view(), name="cliente-delete"),
    path('<int:pk>/',ShowClient.as_view(), name="cliente-detail"),
    path('<int:pk>/update/',ClientUpdateView.as_view(), name="cliente-update"),
    path('listP/',ProveedorListView.as_view(), name="proveedor-list"),
    path('createP/',ProveedorCreateView.as_view(), name="proveedor-create"),
]

