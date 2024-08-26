from django import forms
from .models import Paciente
from main.models import TipoPaciente, Tratamiento  

class PacienteForm(forms.ModelForm):
    class Meta:
        model = Paciente
        fields = ['nombre_paciente', 'sexo_paciente', 'fecha_nacimiento_paciente', 'color_paciente', 'observacion_paciente', 'tipo_paciente', 'tipo_tratamiento']
        labels = {
            'nombre_paciente': 'Nombre del Paciente',
            'sexo_paciente': 'Sexo',
            'fecha_nacimiento_paciente': 'Fecha de Nacimiento',
            'color_paciente': 'Color',
            'observacion_paciente': 'Observaciones',
            'tipo_paciente': 'Tipo de Paciente',
            'tipo_tratamiento': 'Tipo de Tratamiento',
        }
        widgets = {
            'tipo_paciente': forms.Select(attrs={'class': 'form-control'}),
            'tipo_tratamiento': forms.Select(attrs={'class': 'form-control'}),
        }
        # Asegúrate de que tipo_tratamiento sea requerido si es necesario
        required_fields = ['tipo_tratamiento']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['tipo_paciente'].queryset = TipoPaciente.objects.all()
        self.fields['tipo_tratamiento'].queryset = Tratamiento.objects.all()