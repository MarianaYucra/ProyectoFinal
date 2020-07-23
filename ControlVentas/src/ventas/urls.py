from django.urls import path
from . import views
from .views import (VentaListView, VentaDetailView, VentaUpdateView)


app_name = 'ventas'
urlpatterns = [
    path('', views.index, name="index"),
    #path('listar/', views.listar, name = "listar"),
    path('ventas/',VentaListView.as_view(),name = 'venta-list'),
    path('ventas/<int:pk>', VentaDetailView.as_view(), name = 'venta-detail'),
    path('ventas/<int:pk>/update/',VentaUpdateView.as_view(),name = 'venta-update'),

]
