from django.urls import path
from . import views

from .views import (ProductoListView, ProductoDetailView, ProductoCreateView, ProductoUpdateView, ProductoDeleteView, CategoriaListView, CategoriaDetailView, CategoriaCreateView, CategoriaUpdateView, CategoriaDeleteView)

app_name = 'productos'
urlpatterns = [
    #path('listarProducto/', views.listarProducto, name = "listarProducto"),
    #path('listarCategoria/', views.listarCategoria, name = "listarCategoria"),
    path('',ProductoListView.as_view(),name = 'producto-list'),
    path('<int:pk>', ProductoDetailView.as_view(), name = 'producto-detail'),
    path('createProducto/',ProductoCreateView.as_view(),name = 'producto-create'),
    path('<int:pk>/update/',ProductoUpdateView.as_view(),name = 'producto-update'),
    path('<int:pk>/delete/',ProductoDeleteView.as_view(),name = 'producto-delete'),

    path('categoria/',CategoriaListView.as_view(),name = 'categoria-list'),
    path('categoria/<int:pk>', CategoriaDetailView.as_view(), name = 'categoria-detail'),
    path('categoria/createCategoria/',CategoriaCreateView.as_view(),name = 'categoria-create'),
    path('categoria/<int:pk>/update/',CategoriaUpdateView.as_view(),name = 'categoria-update'),
    path('categoria/<int:pk>/delete/',CategoriaDeleteView.as_view(),name = 'categoria-delete'),
]

