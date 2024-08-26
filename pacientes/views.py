from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import PacienteForm
from .models import Paciente
from main.models import TipoPaciente
from roll.models import TipoUsuario

@login_required
def crear_editar_paciente(request, paciente_id=None):
    if paciente_id:
        paciente = get_object_or_404(Paciente, id=paciente_id)
    else:
        paciente = None

    if request.method == 'POST':
        form = PacienteForm(request.POST, instance=paciente)
        if form.is_valid():
            paciente = form.save(commit=False)
            paciente.cliente = request.user.cliente  # Asocia el paciente al cliente actual
            paciente.save()
            return redirect('ver_paciente')  # Redirige a la lista de pacientes después de guardar
    else:
        form = PacienteForm(instance=paciente)

    return render(request, 'pacientes/crear_editar_paciente.html', {'form': form, 'paciente': paciente})


@login_required
def ver_paciente(request):
    cliente = request.user.cliente  # Ensure the client is associated with the user
    pacientes = Paciente.objects.filter(cliente=cliente)

    # Retrieve TipoUsuario associated with the user
    try:
        tipo_usuario = TipoUsuario.objects.get(usuario=request.user)
    except TipoUsuario.DoesNotExist:
        tipo_usuario = None

    context = {
        'pacientes': pacientes,
        'tipo_usuario': tipo_usuario.tipo if tipo_usuario else None,
    }

    return render(request, 'pacientes/ver_paciente.html', context)


@login_required
def eliminar_paciente(request, paciente_id):
    paciente = get_object_or_404(Paciente, id=paciente_id)
    if request.method == 'POST':
        paciente.delete()
        return redirect('ver_paciente')
    return render(request, 'pacientes/confirmar_eliminar_paciente.html', {'paciente': paciente})


