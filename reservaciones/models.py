from django.contrib.auth.models import User
from django.db import models

from servicios.models import Evento, Servicio
from tinocoloco_app.models import Cliente


class Alquiler(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    evento = models.ForeignKey(Evento, on_delete=models.CASCADE)
    fecha_alquiler = models.DateField()
    hora_inicio_reserva = models.TimeField()
    hora_fin_planificada_reserva = models.TimeField()
    hora_fin_real_reserva = models.TimeField(null=True, blank=True)
    costo_alquiler = models.DecimalField(max_digits=10, decimal_places=2)
    calificacion_cliente = models.IntegerField(null=True, blank=True)
    calificacion_negocio = models.IntegerField(null=True, blank=True)
    observacion = models.TextField(blank=True)

    def __str__(self):
        return f"Alquiler {self.id} - {self.evento}"


class AlquilerServicio(models.Model):
    alquiler = models.ForeignKey(Alquiler, on_delete=models.CASCADE)
    servicio = models.ForeignKey(Servicio, on_delete=models.CASCADE)
    cantidad = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.servicio} para Alquiler {self.alquiler.id}"


class Reserva(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    servicio = models.ForeignKey(Servicio, on_delete=models.CASCADE)
    fecha_evento = models.DateField()
    direccion = models.TextField()
    telefono = models.CharField(max_length=20)
    fecha_creacion = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Reserva de {self.usuario.username} para {self.servicio.nombre} el {self.fecha_evento}"
