from django.contrib import admin
from .models import Serie, Reseña, Episodio, Etiqueta  # Asegúrate de importar todos los modelos necesarios
from django import forms

# Configuración de admin para el modelo Serie
class SerieAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'fecha_lanzamiento', 'genero', 'numero_episodios')
    search_fields = ('titulo', 'genero', 'creador')
    list_filter = ('genero', 'fecha_lanzamiento')
    ordering = ('-fecha_lanzamiento',)

# Configuración de admin para el modelo Reseña
class ReseñaAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'serie', 'usuario', 'calificacion', 'fecha_creacion')
    search_fields = ('titulo', 'contenido', 'usuario__username', 'serie__titulo')
    list_filter = ('calificacion', 'fecha_creacion')
    ordering = ('-fecha_creacion',)
    raw_id_fields = ('serie', 'usuario')  # Para seleccionar series y usuarios mediante IDs en lugar de desplegables grandes

# Configuración de admin para el modelo Episodio
class EpisodioAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'serie', 'numero_episodio', 'fecha_emision')
    search_fields = ('titulo', 'serie__titulo')
    list_filter = ('fecha_emision', 'serie')
    ordering = ('-fecha_emision',)

# Configuración de admin para el modelo Etiqueta
class EtiquetaAdmin(admin.ModelAdmin):
    list_display = ('nombre',)
    search_fields = ('nombre',)
    
class EpisodioInline(admin.TabularInline):
    model = Episodio
    extra = 1  # Número de formularios adicionales en blanco

class SerieAdmin(admin.ModelAdmin):
    inlines = [EpisodioInline]

# Registrar los modelos en el administrador
admin.site.register(Serie, SerieAdmin)
admin.site.register(Reseña, ReseñaAdmin)
admin.site.register(Episodio, EpisodioAdmin)
admin.site.register(Etiqueta, EtiquetaAdmin)

def marcar_como_destacado(modeladmin, request, queryset):
    queryset.update(destacado=True)

marcar_como_destacado.short_description = "Marcar series seleccionadas como destacadas"

class SerieAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'fecha_lanzamiento', 'genero', 'numero_episodios', 'destacado')
    actions = [marcar_como_destacado]

class SerieForm(forms.ModelForm):
    class Meta:
        model = Serie
        fields = '__all__'
        widgets = {
            'descripcion': forms.Textarea(attrs={'rows': 4, 'cols': 40}),
        }

class SerieAdmin(admin.ModelAdmin):
    form = SerieForm