from django import forms

from .models import Evento, Servicio


class EventoForm(forms.ModelForm):
    class Meta:
        model = Evento
        fields = ['tipo_evento', 'descripcion', 'valor_referencial', 'numero_horas_permitidas', 'valor_extra_hora']


class ServicioForm(forms.ModelForm):
    class Meta:
        model = Servicio
        fields = ['nombre', 'descripcion', 'imagen', 'precio']
