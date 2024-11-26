from django.urls import path

from . import views

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('registrarse/', views.registrarse, name='registrarse'),
    path('iniciar_sesion/', views.iniciar_sesion, name='iniciar_sesion'),
    path('cerrar_sesion/', views.cerrar_sesion, name='cerrar_sesion'),
    path('sobre_nosotros/', views.sobre_nosotros, name='sobre_nosotros'),
]
