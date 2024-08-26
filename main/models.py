from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Region(models.Model):
    codigo = models.CharField(max_length=10, blank=True)
    tipo = models.CharField(max_length=100, blank=True)
    nombre = models.CharField(max_length=100, blank=True)
    lat = models.FloatField(null=True)
    lng = models.FloatField(null=True)
    url = models.URLField(blank=True)  # Podría estar en blanco
    codigo_padre = models.CharField(max_length=10, blank=True)  # Podría estar en blanco

    def __str__(self):
        return self.nombre

class Provincia(models.Model):
    codigo = models.CharField(max_length=10, blank=True)
    tipo = models.CharField(max_length=100, blank=True)
    nombre = models.CharField(max_length=100, blank=True)
    lat = models.FloatField(null=True)
    lng = models.FloatField(null=True)
    url = models.URLField(blank=True)  # Podría estar en blanco
    codigo_padre = models.CharField(max_length=10, blank=True)  # Podría estar en blanco
    region = models.ForeignKey(Region, null=True, blank=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre

class Comuna(models.Model):
    codigo = models.CharField(max_length=10, blank=True)
    tipo = models.CharField(max_length=100, blank=True)
    nombre = models.CharField(max_length=100, blank=True)
    lat = models.FloatField(null=True)
    lng = models.FloatField(null=True)
    url = models.URLField(blank=True)  # Podría estar en blanco
    codigo_padre = models.CharField(max_length=10, blank=True)  # Podría estar en blanco
    provincia = models.ForeignKey(Provincia, null=True, blank=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre

class EstadoCivil(models.Model):
    tipo_estado_civil = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.tipo_estado_civil

class Cliente(models.Model):
    numrut_cliente = models.CharField(max_length=12, primary_key=True, blank=True)
    telefono_cliente = models.CharField(max_length=15, null=True, blank=True)
    direccion_cliente = models.CharField(max_length=50, null=True, blank=True)
    comuna = models.ForeignKey(Comuna, on_delete=models.CASCADE, null=True, blank=True)
    estado_civil = models.ForeignKey(EstadoCivil, on_delete=models.CASCADE, null=True, blank=True)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.numrut_cliente

class Sucursal(models.Model):
    nombre_clinica = models.CharField(max_length=50)
    direccion_clinica = models.CharField(max_length=200)
    comuna = models.ForeignKey(Comuna, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.nombre_clinica} {self.direccion_clinica}"


class Especialidad(models.Model):
    nombre_especialidad = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre_especialidad

class Veterinario(models.Model):
    numrut_veterinario = models.CharField(max_length=12, primary_key=True)
    nombre_veterinario = models.CharField(max_length=50)
    apellido_veterinario = models.CharField(max_length=50)
    correo_veterinario = models.CharField(max_length=50, null=True, blank=True)
    direccion_veterinario = models.CharField(max_length=50)
    telefono_veterinario = models.CharField(max_length=15)
    comuna = models.ForeignKey(Comuna, on_delete=models.CASCADE)
    estado_civil = models.ForeignKey(EstadoCivil, on_delete=models.CASCADE)
    especialidad = models.ForeignKey(Especialidad, on_delete=models.CASCADE)    
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    sucursal = models.ForeignKey(Sucursal, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.nombre_veterinario} {self.apellido_veterinario}"
 

class Recepcionista(models.Model):
    numrut_recepcionista = models.CharField(max_length=12, primary_key=True)
    nombre_recepcionista = models.CharField(max_length=50)
    apellido_recepcionista = models.CharField(max_length=50)
    correo_recepcionista = models.CharField(max_length=50, null=True, blank=True)
    direccion_recepcionista = models.CharField(max_length=50)
    telefono_recepcionista = models.CharField(max_length=15)
    comuna = models.ForeignKey(Comuna, on_delete=models.CASCADE)
    estado_civil = models.ForeignKey(EstadoCivil, on_delete=models.CASCADE)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.nombre_recepcionista} {self.apellido_recepcionista}"

class RazaPaciente(models.Model):
    RAZA_CHOICES = [
        ('perro', 'Perro'),
        ('gato', 'Gato'),
        ('ave', 'Ave')
    ]
    raza_paciente = models.CharField(max_length=10, choices=RAZA_CHOICES)
    raza_perro = models.CharField(max_length=50, null=True, blank=True)
    raza_gato = models.CharField(max_length=50, null=True, blank=True)
    raza_ave = models.CharField(max_length=50, null=True, blank=True)

    def __str__(self):
        return f"{self.raza_paciente}: {self.raza_perro or self.raza_gato or self.raza_ave}"

class TipoPaciente(models.Model):
    tipo_paciente = models.CharField(max_length=50)
    raza_paciente = models.ForeignKey(RazaPaciente, on_delete=models.CASCADE)

    def __str__(self):
        return self.tipo_paciente

class Tratamiento(models.Model):
    tipo_tratamiento = models.CharField(max_length=50, unique=True, null=True, blank=True)

    def __str__(self):
        return self.tipo_tratamiento
    

class Contacto(models.Model):
    nombre = models.CharField(max_length=100)
    email = models.EmailField()
    telefono = models.CharField(max_length=20)
    mensaje = models.TextField()

    def __str__(self):
        return self.nombre    


def get_cliente(self):
    try:
        return Cliente.objects.get(usuario=self)
    except Cliente.DoesNotExist:
        return None

User.add_to_class('cliente', property(get_cliente))    
