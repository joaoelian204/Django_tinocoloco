from django.urls import path

from . import views

urlpatterns = [
    path('', views.lista_servicios, name='lista_servicios'),
    path('<int:servicio_id>/', views.detalle_servicio, name='detalle_servicio'),
    path('eventos/', views.listar_eventos, name='listar_eventos'),
    path('eventos/crear/', views.crear_evento, name='crear_evento'),
    path('eventos/<int:pk>/editar/', views.editar_evento, name='editar_evento'),
    path('eventos/<int:pk>/eliminar/', views.eliminar_evento, name='eliminar_evento'),
]
