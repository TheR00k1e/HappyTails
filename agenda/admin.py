from django.contrib import admin
from .models import HorarioVeterinario, Cita
from django.forms.widgets import TimeInput
from django import forms

# Define el formulario personalizado para el HorarioVeterinario
class HorarioVeterinarioForm(forms.ModelForm):
    class Meta:
        model = HorarioVeterinario
        fields = '__all__'
        widgets = {
            'hora_inicio_manana': TimeInput(format='%H:%M'),
            'hora_fin_manana': TimeInput(format='%H:%M'),
            'hora_inicio_tarde': TimeInput(format='%H:%M'),
            'hora_fin_tarde': TimeInput(format='%H:%M'),
        }

# Registra el modelo Cita en el administrador de Django
@admin.register(Cita)
class CitaAdmin(admin.ModelAdmin):    
    pass