from django.db import models
from main.models import Sucursal, Veterinario
from django.contrib.auth.models import User
from datetime import date, time
from django.core.exceptions import ValidationError

# Create your models here.

def validar_dia(value):
    if not isinstance(value, date):
        raise ValidationError('El valor debe ser una fecha.')
    
    today = date.today()

    if value < today:
        raise ValidationError('No es posible elegir una fecha anterior al día actual.')


class Cita(models.Model):
    fecha_cita = models.DateField(help_text="Ingrese un fecha para la agenda", validators=[validar_dia])
    sucursal = models.ForeignKey(Sucursal, on_delete=models.CASCADE)
    veterinario = models.ForeignKey(Veterinario, on_delete=models.CASCADE)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)

    HORARIOS = (
        ("1","09:00 hasta 10:00"),
        ("2","10:00 hasta 11:00"),
        ("3","11:00 hasta 12:00"),
        ("4","12:00 hasta 13:00"),
        ("5","13:00 hasta 14:00"),
        ("6","14:00 hasta 15:00"),
        ("7","15:00 hasta 16:00"),
        ("8","16:00 hasta 17:00"),
        ("9","17:00 hasta 18:00"),
        ("10","18:00 hasta 19:00"),
        ("11","19:00 hasta 20:00"),
    )
    horario = models.CharField(max_length=10, choices=HORARIOS, default="1")

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['horario', 'fecha_cita', 'veterinario', 'sucursal'], name='unique_cita')
        ]

    def __str__(self):
        return f'{self.fecha_cita.strftime("%Y-%m-%d")} - {self.get_horario_display()} - {self.veterinario}'


class HorarioVeterinario(models.Model):
    veterinario = models.ForeignKey(Veterinario, on_delete=models.CASCADE)
    dia_semana = models.CharField(max_length=10)  # Ejemplo: "Lunes", "Martes", etc.
    hora_inicio_manana = models.TimeField(default=time(9, 0))
    hora_fin_manana = models.TimeField(default=time(12, 0))
    hora_inicio_tarde = models.TimeField(default=time(13, 0))
    hora_fin_tarde = models.TimeField(default=time(18, 0))

    def __str__(self):
        return f"Horario de {self.veterinario.nombre_veterinario} {self.veterinario.apellido_veterinario} - {self.dia_semana}"
    
    def horarios_validos(self):
        horarios = []
        if self.hora_inicio_manana != time(0, 0) and self.hora_fin_manana != time(0, 0):
            horarios.append((self.hora_inicio_manana, self.hora_fin_manana, self.dia_semana))
        if self.hora_inicio_tarde != time(0, 0) and self.hora_fin_tarde != time(0, 0):
            horarios.append((self.hora_inicio_tarde, self.hora_fin_tarde, self.dia_semana))
        return horarios