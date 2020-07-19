from django.urls import path
from . import views

urlpatterns = [
    path('listarProducto/', views.listarProducto, name = "listarProducto"),
    path('listarCategoria/', views.listarCategoria, name = "listarCategoria"),
]

