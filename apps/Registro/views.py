from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Serie, Episodio, Reseña
from .forms import ReseñaForm

def index(request):
    """Vista para la página de inicio."""
    return render(request, 'base.html')

def lista_series(request):
    """Vista para listar todas las series."""
    series = Serie.objects.all()
    return render(request, 'lista_series.html', {'series': series})

def detalle_serie(request, serie_id):
    """Vista para mostrar detalles de una serie específica."""
    serie = get_object_or_404(Serie, id=serie_id)
    episodios = serie.episodios.all()
    reseñas = serie.reseñas.all()
    return render(request, 'detalle_serie.html', {
        'serie': serie,
        'episodios': episodios,
        'reseñas': reseñas,
    })

def detalle_episodio(request, serie_id, episodio_id):
    """Vista para mostrar detalles de un episodio específico."""
    episodio = get_object_or_404(Episodio, id=episodio_id, serie_id=serie_id)
    reseñas = episodio.reseñas.all()
    return render(request, 'detalle_episodio.html', {
        'episodio': episodio,
        'reseñas': reseñas,
    })

def lista_reseñas(request):
    """Vista para listar todas las reseñas."""
    reseñas = Reseña.objects.all()
    return render(request, 'lista_reseñas.html', {'reseñas': reseñas})

def detalle_reseña(request, reseña_id):
    """Vista para mostrar detalles de una reseña específica."""
    reseña = get_object_or_404(Reseña, id=reseña_id)
    return render(request, 'detalle_reseña.html', {'reseña': reseña})

@login_required
def crear_reseña(request):
    """Vista para crear una nueva reseña."""
    if request.method == 'POST':
        form = ReseñaForm(request.POST)
        if form.is_valid():
            reseña = form.save(commit=False)
            reseña.usuario = request.user  # Asigna el usuario actual a la reseña
            reseña.save()
            return redirect('detalle_reseña', reseña_id=reseña.id)
    else:
        form = ReseñaForm()
    
    return render(request, 'formulario_reseña.html', {'form': form})
