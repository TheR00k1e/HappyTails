from django.contrib.auth.models import User
from django.db import models

class TipoUsuario(models.Model):
    usuario = models.OneToOneField(User, on_delete=models.CASCADE)
    tipo = models.CharField(max_length=50, default='cliente')

    def __str__(self):
        return self.tipo
