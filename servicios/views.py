from django.contrib import messages
from django.shortcuts import get_object_or_404, redirect, render

from .forms import EventoForm
from .models import Evento, Servicio


def lista_servicios(request):
    """
    Muestra todos los servicios disponibles.
    """
    servicios = Servicio.objects.all()
    return render(request, 'servicios/lista_servicios.html', {'servicios': servicios})


def detalle_servicio(request, servicio_id):
    """
    Muestra los detalles de un servicio, incluyendo sus imágenes adicionales.
    """
    servicio = get_object_or_404(Servicio, id=servicio_id)
    fotos = servicio.fotos.all()
    return render(request, 'servicios/detalle_servicio.html', {
        'servicio': servicio,
        'fotos': fotos,
    })


def listar_eventos(request):
    """
    Lista todos los eventos.
    """
    eventos = Evento.objects.all()
    return render(request, 'servicios/listar_eventos.html', {'eventos': eventos})


def crear_evento(request):
    """
    Crea un nuevo evento.
    """
    if request.method == 'POST':
        form = EventoForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Evento creado exitosamente.')
            return redirect('listar_eventos')
    else:
        form = EventoForm()
    return render(request, 'servicios/crear_evento.html', {'form': form})


def editar_evento(request, pk):
    """
    Edita un evento existente.
    """
    evento = get_object_or_404(Evento, pk=pk)
    if request.method == 'POST':
        form = EventoForm(request.POST, instance=evento)
        if form.is_valid():
            form.save()
            return redirect('listar_eventos')
    else:
        form = EventoForm(instance=evento)
    return render(request, 'servicios/editar_evento.html', {'form': form})


def eliminar_evento(request, pk):
    """
    Elimina un evento.
    """
    evento = get_object_or_404(Evento, pk=pk)
    if request.method == 'POST':
        evento.delete()
        messages.success(request, 'Evento eliminado exitosamente.')
        return redirect('listar_eventos')
    return render(request, 'servicios/eliminar_evento.html', {'evento': evento})
