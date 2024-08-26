from django.contrib import admin
from .models import *

# Register your models here.

@admin.register(Region)
class RegionAdmin(admin.ModelAdmin):
    pass

@admin.register(Provincia)
class ProvinciaAdmin(admin.ModelAdmin):
    pass

@admin.register(Comuna)
class ComunaAdmin(admin.ModelAdmin):
    pass

@admin.register(EstadoCivil)
class EstadoCivilAdmin(admin.ModelAdmin):
    pass

@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):
    pass

@admin.register(Sucursal)
class SucursalAdmin(admin.ModelAdmin):
    pass

@admin.register(Especialidad)
class EspecialidadAdmin(admin.ModelAdmin):
    pass

@admin.register(Veterinario)
class VeterinarioAdmin(admin.ModelAdmin):
    pass

@admin.register(Recepcionista)
class RecepcionistaAdmin(admin.ModelAdmin):
    pass

@admin.register(RazaPaciente)
class RazaPacienteAdmin(admin.ModelAdmin):
    pass

@admin.register(TipoPaciente)
class TipoPacienteAdmin(admin.ModelAdmin):
    pass

@admin.register(Tratamiento)
class TratamientoAdmin(admin.ModelAdmin):
    pass


@admin.register(Contacto)
class ContactAdmin(admin.ModelAdmin):
    pass