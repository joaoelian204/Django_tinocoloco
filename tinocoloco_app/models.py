from django.contrib.auth.models import User
from django.db import models


class Cliente(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    identificacion = models.CharField(max_length=20)
    nacionalidad = models.CharField(max_length=100)
    telefono = models.CharField(max_length=20)
    fecha_registro = models.DateTimeField(auto_now_add=True)
    genero = models.CharField(max_length=20, choices=(("M", "Masculino"), ("F", "Femenino")))

    def __str__(self):
        return f"{self.user.get_full_name()}"

