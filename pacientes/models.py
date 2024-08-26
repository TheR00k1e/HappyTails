from django.db import models
from main.models import Cliente, TipoPaciente, Tratamiento

class Paciente(models.Model):
    nombre_paciente = models.CharField(max_length=50)
    sexo_paciente = models.BooleanField(choices=[(True, 'Masculino'), (False, 'Femenino')])
    fecha_nacimiento_paciente = models.DateField()
    color_paciente = models.CharField(max_length=25)
    observacion_paciente = models.TextField()
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE, related_name='pacientes')
    tipo_paciente = models.ForeignKey(TipoPaciente, on_delete=models.CASCADE, related_name='pacientes')
    tipo_tratamiento = models.ForeignKey(Tratamiento, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre_paciente
