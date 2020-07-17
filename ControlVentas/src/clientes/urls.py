from django.urls import path
from . import views
from .views import (
        ClientListView,
        ShowClient,
        ClientCreateView,
        ClientDeleteView,
        ClientUpdateView,
        )

urlpatterns = [
    path('lista/',views.showListClient, name="listaCliente"),
    path('añadir/',views.newClient, name="nuevoCliente"),
    path('list/',ClientListView.as_view(), name="cliente-list"),
    path('create/',ClientCreateView.as_view(), name="cliente-create"),
    path('<int:pk>/delete/',ClientDeleteView.as_view(), name="cliente-delete"),
    path('<int:pk>/',ShowClient.as_view(), name="cliente-detail"),
    path('<int:pk>/update/',ClientUpdateView.as_view(), name="cliente-update"),
]

