from cloudinary.models import CloudinaryField
from django.db import models


class TipoEvento(models.Model):
    nombreevento = models.CharField(max_length=100)

    def __str__(self):
        return self.nombreevento


class Evento(models.Model):
    tipo_evento = models.ForeignKey(TipoEvento, on_delete=models.CASCADE)
    descripcion = models.TextField()
    valor_referencial = models.DecimalField(max_digits=10, decimal_places=2)
    numero_horas_permitidas = models.PositiveIntegerField()
    valor_extra_hora = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.tipo_evento} - {self.descripcion}"


class Servicio(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    imagen = models.ImageField(upload_to='servicios/')
    precio = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.nombre


class FotoEvento(models.Model):
    servicio = models.ForeignKey(Servicio, on_delete=models.CASCADE, related_name='fotos')
    imagen = CloudinaryField('imagen')
    descripcion = models.CharField(max_length=255)

    def __str__(self):
        return f"Foto de {self.servicio.nombre} - {self.descripcion}"


