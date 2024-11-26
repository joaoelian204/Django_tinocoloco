from django.contrib import admin

from .models import Evento, FotoEvento, Servicio, TipoEvento


class FotoEventoInline(admin.TabularInline):
    model = FotoEvento
    extra = 6  # Permite agregar múltiples fotos desde el administrador


class ServicioAdmin(admin.ModelAdmin):
    inlines = [FotoEventoInline]


admin.site.register(TipoEvento)
admin.site.register(Evento)
admin.site.register(Servicio, ServicioAdmin)


