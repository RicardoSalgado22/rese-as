from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('series/', views.lista_series, name='lista_series'),
    path('series/<int:serie_id>/', views.detalle_serie, name='detalle_serie'),
    path('series/<int:serie_id>/episodios/<int:episodio_id>/', views.detalle_episodio, name='detalle_episodio'),
    path('reseñas/', views.lista_reseñas, name='lista_reseñas'),
    path('reseñas/<int:reseña_id>/', views.detalle_reseña, name='detalle_reseña'),
    path('reseñas/nueva/', views.crear_reseña, name='crear_reseña'),
]
