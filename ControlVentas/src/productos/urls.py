from django.urls import path
from . import views

from .views import (ProductoListView, ProductoCreateView,)

app_name = 'productos'
urlpatterns = [
    #path('listarProducto/', views.listarProducto, name = "listarProducto"),
    #path('listarCategoria/', views.listarCategoria, name = "listarCategoria"),
    path('',ProductoListView.as_view(),name = 'producto-list'),
    path('createProducto/',ProductoCreateView.as_view(),name = 'producto-create'),
]

