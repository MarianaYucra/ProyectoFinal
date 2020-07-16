from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('añadir/',views.newRecord, name="nuevoRegistro"),
    path('administrar',views.administration, name="administrar"),

]
