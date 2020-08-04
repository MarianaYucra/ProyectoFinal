from django.urls import path
from . import views
from .views import (VentaListView, VentaDetailView, VentaUpdateView)


app_name = 'ventas'
urlpatterns = [
    path('', views.index, name="index"),
    #path('añadir/',views.newRecord, name="nuevoRegistro"),
    path('administrar',views.administration, name="administrar"),
    #path('listar/', views.listar, name = "listar"),
    path('ventas/',VentaListView.as_view(),name = 'venta-list'),
<<<<<<< HEAD
    #path('ventas/<int:pk>', VentaDetailView.as_view(), name = 'venta-detail'),
    #path('ventas/<int:pk>/update/',VentaUpdateView.as_view(),name = 'venta-update'),

=======
    path('ventas/<int:pk>', VentaDetailView.as_view(), name = 'venta-detail'),
    path('ventas/<int:pk>/update/',VentaUpdateView.as_view(),name = 'venta-update'),
>>>>>>> df5923b78ffc81bfee55ab9b971f23283b9e0546
]
