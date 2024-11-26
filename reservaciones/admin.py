from django.contrib import admin

from .models import Alquiler, AlquilerServicio, Reserva

admin.site.register(Reserva)
admin.site.register(Alquiler)
admin.site.register(AlquilerServicio)

