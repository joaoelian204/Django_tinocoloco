from django import forms

from .models import Alquiler, Reserva


class ReservaForm(forms.ModelForm):
    class Meta:
        model = Reserva
        fields = ['fecha_evento', 'direccion', 'telefono']
        widgets = {'fecha_evento': forms.DateInput(attrs={'type': 'date'})}
        labels = {
            'fecha_evento': 'Fecha del Evento',
            'direccion': 'Dirección del Evento',
            'telefono': 'Teléfono de Contacto',
        }


class AlquilerForm(forms.ModelForm):
    class Meta:
        model = Alquiler
        fields = ['cliente', 'evento', 'fecha_alquiler', 'hora_inicio_reserva', 'hora_fin_planificada_reserva',
                'costo_alquiler', 'calificacion_cliente', 'calificacion_negocio', 'observacion']
