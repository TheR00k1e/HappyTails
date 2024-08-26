from django import forms
from .models import Cita
from main.models import Sucursal

class CitaForm(forms.ModelForm):
    class Meta:
        model = Cita
        fields = ['veterinario', 'sucursal', 'fecha_cita', 'horario']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['sucursal'].label_from_instance = lambda obj: f"{obj.nombre_clinica} - {obj.direccion_clinica}"