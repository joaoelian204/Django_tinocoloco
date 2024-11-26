from django.urls import path

from . import views

urlpatterns = [
    path('<int:servicio_id>/reservar/', views.reservar_servicio, name='reservar_servicio'),
    path('mostrar-mensaje/', views.mostrar_mensaje, name='mostrar_mensaje'),  # Corrige aquí
]
