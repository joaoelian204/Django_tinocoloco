from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.shortcuts import redirect, render


def inicio(request):
    return render(request, 'tinocoloco_app/inicio.html')

def registrarse(request):
    if request.method == 'GET':
        return render(request, 'tinocoloco_app/registrarse.html', {
            'form': UserCreationForm
        })
    else:
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.create_user(
                    username=request.POST['username'],
                    password=request.POST['password1']
                )
                user.save()
                login(request, user)
                return redirect('inicio')
            except IntegrityError:
                return render(request, 'tinocoloco_app/registrarse.html', {
                    'form': UserCreationForm,
                    'error': 'El usuario ya existe'
                })
        return render(request, 'tinocoloco_app/registrarse.html', {
            'form': UserCreationForm,
            'error': 'Las contraseñas no coinciden'
        })


def iniciar_sesion(request):
    if request.method == 'GET':
        return render(request, 'tinocoloco_app/iniciar_sesion.html', {
            'form': AuthenticationForm
        })
    else:
        user = authenticate(
            request, username=request.POST['username'], password=request.POST['password']
        )
        if user is None:
            return render(request, 'tinocoloco_app/iniciar_sesion.html', {
                'form': AuthenticationForm,
                'error': 'Usuario o contraseña incorrectos'
            })
        else:
            login(request, user)
            return redirect('inicio')


def cerrar_sesion(request):
    logout(request)
    return redirect('inicio')


def sobre_nosotros(request):
    return render(request, 'tinocoloco_app/sobre_nosotros.html')
