from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render

from .forms import ReservaForm
from .models import Servicio


@login_required(login_url='/reservaciones/mostrar-mensaje/')
def reservar_servicio(request, servicio_id):
    """
    Permite al usuario reservar un servicio.
    """
    servicio = get_object_or_404(Servicio, id=servicio_id)

    if request.method == 'POST':
        form = ReservaForm(request.POST)
        if form.is_valid():
            reserva = form.save(commit=False)
            reserva.usuario = request.user
            reserva.servicio = servicio
            reserva.save()
            return redirect('lista_servicios')
    else:
        form = ReservaForm()

    return render(request, 'reservaciones/reservar_servicio.html', {
        'form': form,
        'servicio': servicio
    })


def mostrar_mensaje(request):
    """
    Muestra una página indicando que el usuario no está autenticado.
    """
    return render(request, 'reservaciones/no_registrado.html')
