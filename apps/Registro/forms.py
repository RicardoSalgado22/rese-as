from django import forms
from .models import Reseña

class ReseñaForm(forms.ModelForm):
    class Meta:
        model = Reseña
        fields = ['serie', 'episodio', 'titulo', 'contenido', 'calificacion']
