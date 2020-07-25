from django.urls import path
from . import views
from .views import ( ClientListView, ShowClient, ClientCreateView, ClientDeleteView, ClientUpdateView,
        ProveedorListView, ProveedorCreateView, ProveedorDeleteView, ProveedorDetailView, ProveedorUpdateView,
        ContactListView, ContactCreateView, ContactDeleteView, ContactDetailView, ContactUpdateView,
        )

app_name = 'clientes'
urlpatterns = [
    path('lista/',views.showListClient, name="listaCliente"),
    path('añadir/',views.newClient, name="nuevoCliente"),
    path('list/',ClientListView.as_view(), name="cliente-list"),
    path('create/',ClientCreateView.as_view(), name="cliente-create"),
    path('<int:pk>/delete/',ClientDeleteView.as_view(), name="cliente-delete"),
    path('<int:pk>/detail/',ShowClient.as_view(), name="cliente-detail"),
    path('<int:pk>/update/',ClientUpdateView.as_view(), name="cliente-update"),

    path('listP/',ProveedorListView.as_view(), name="proveedor-list"),
    path('createP/',ProveedorCreateView.as_view(), name="proveedor-create"),
    path('<int:pk>/deleteP/',ProveedorDeleteView.as_view(), name="proveedor-delete"),
    path('<int:pk>/detailP/',ProveedorDetailView.as_view(), name="proveedor-detail"),
    path('<int:pk>/updateP/',ProveedorUpdateView.as_view(), name="proveedor-update"),
    
    path('listC/',ContactListView.as_view(), name="contacto-list"),
    path('createC/',ContactCreateView.as_view(), name="contacto-create"),
    path('<int:pk>/deleteC/',ContactDeleteView.as_view(), name="contact-delete"),
    path('<int:pk>/detailC/',ContactDetailView.as_view(), name="contacto-detail"),
    path('<int:pk>/updateC/',ContactUpdateView.as_view(), name="contacto-update"),
]

