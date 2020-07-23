from django.urls import path
from . import views
from .views import (VentaListView, VentaDetailView, VentaUpdateView)


app_name = 'ventas'
urlpatterns = [
    path('', views.index, name="index"),
<<<<<<< HEAD
    path('añadir/',views.newRecord, name="nuevoRegistro"),
    path('administrar',views.administration, name="administrar"),
=======
    #path('listar/', views.listar, name = "listar"),
    path('ventas/',VentaListView.as_view(),name = 'venta-list'),
    path('ventas/<int:pk>', VentaDetailView.as_view(), name = 'venta-detail'),
    path('ventas/<int:pk>/update/',VentaUpdateView.as_view(),name = 'venta-update'),
>>>>>>> d36dfedb4a121a7bde8cf1726ec84cae214f0a78

]
