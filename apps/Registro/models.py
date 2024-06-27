from django.db import models
from django.contrib.auth.models import User  # Asumiendo que usarás el modelo de usuario predeterminado de Django

class Etiqueta(models.Model):
    nombre = models.CharField(max_length=50, unique=True)
    
    def __str__(self):
        return self.nombre

class Serie(models.Model):
    titulo = models.CharField(max_length=255)
    descripcion = models.TextField()
    fecha_lanzamiento = models.DateField()
    genero = models.CharField(max_length=100)  # Podrías usar una elección de géneros predefinidos.
    numero_episodios = models.PositiveIntegerField()
    duracion_episodio = models.PositiveIntegerField(help_text="Duración promedio de episodios en minutos")
    creador = models.CharField(max_length=255)  # Nombre del creador de la serie
    imagen = models.ImageField(upload_to='static/img/', blank=True, null=True)  # Para cargar imágenes de la serie
    etiquetas = models.ManyToManyField(Etiqueta, related_name='series', blank=True)

    def __str__(self):
        return self.titulo
    
class Episodio(models.Model):
    serie = models.ForeignKey(Serie, on_delete=models.CASCADE, related_name='episodios')
    titulo = models.CharField(max_length=255)
    descripcion = models.TextField()
    numero_episodio = models.PositiveIntegerField()
    fecha_emision = models.DateField()
    duracion = models.PositiveIntegerField(help_text="Duración del episodio en minutos")

    def __str__(self):
        return f'{self.serie.titulo} - {self.titulo} (Episodio {self.numero_episodio})'

class Reseña(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    serie = models.ForeignKey(Serie, on_delete=models.CASCADE, related_name='reseñas')
    titulo = models.CharField(max_length=255)
    contenido = models.TextField()
    calificacion = models.PositiveIntegerField(default=1, choices=[(i, str(i)) for i in range(1, 6)])  # Calificación del 1 al 5
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    etiquetas = models.ManyToManyField(Etiqueta, related_name='reseñas', blank=True)
    episodio = models.ForeignKey(Episodio, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return f'{self.usuario.username} - {self.serie.titulo} - {self.titulo}'
    
