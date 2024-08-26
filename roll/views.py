from django.db import IntegrityError
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate
from .models import TipoUsuario  
from main.models import Cliente
from django.contrib.auth.models import Group
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth import logout as django_logout


# Create your views here.

def signup(request):
    if request.method == 'GET':
        return render(request, 'signup.html', {'form': UserCreationForm()})
    else:
        form = UserCreationForm(request.POST)
        if form.is_valid():
            if request.POST['password1'] == request.POST['password2']:
                try:
                    # Crear el usuario
                    user = User.objects.create_user(
                        username=request.POST['username'], 
                        first_name=request.POST['first_name'],
                        last_name=request.POST['last_name'],
                        email=request.POST['email'], 
                        password=request.POST['password1']
                    )

                    # Asociar al grupo "Cliente" (suponiendo que ya existe)
                    grupo, _ = Group.objects.get_or_create(name='Clientes')
                    user.groups.add(grupo)

                    # Crear el tipo de usuario asociado (en este caso, cliente)
                    tipo_usuario = TipoUsuario.objects.create(usuario=user, tipo='cliente')
                    tipo_usuario.save()

                    # Crear el usuario también en el modelo Cliente
                    cliente = Cliente.objects.create(usuario=user)
                    cliente.save()

                    user.save()

                    # Cerrar la sesión actual del usuario
                    signout(request)

                    # Redirigir a la misma página para limpiar los datos POST
                    return HttpResponseRedirect(reverse('index'))
                except IntegrityError:
                    return render(request, 'signup.html', {
                        'form': UserCreationForm(),
                        'error': 'Usuario ya existe'
                    })
            else:
                return render(request, 'signup.html', {
                    'form': UserCreationForm(),
                    'error': 'Las contraseñas no coinciden'
                })
        else:
            # Imprimir errores del formulario en la consola
            print(form.errors)
            return render(request, 'signup.html', {
                'form': form,
                'error': 'Esta contraseña debe contener al menos 8 caracteres y tiene que ser alfanúmerica'
            })


def signout(request):
    # Cerrar sesión en Django
    django_logout(request)
    
    # Redirigir al usuario a la página de inicio
    response = redirect('index')
    
    # Eliminar csrftoken si está presente
    if 'csrftoken' in request.COOKIES:
        response.delete_cookie('csrftoken')
    
    # Eliminar sessionid si está presente
    if 'sessionid' in request.COOKIES:
        response.delete_cookie('sessionid')

    # Eliminar messages si está presente
    if 'messages' in request.COOKIES:
        response.delete_cookie('messages')

    return response



def signin(request):
    if request.method == 'GET':
        return render(request, 'signin.html', {'form': AuthenticationForm})
    else:
        user = authenticate(request, username=request.POST['username'], password=request.POST['password'])
        if user is None:
            return render(request, 'signin.html', {'form': AuthenticationForm, 'error': 'Usuario o contraseña es incorrecta'})
        else:
            login(request, user)
            return redirect('index')
