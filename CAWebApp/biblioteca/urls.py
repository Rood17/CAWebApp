from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    # Path de biblioteca
    path('', views.biblioteca, name='biblioteca'),
    path('biblio-index/', views.biblioIndex, name="biblio-index"),

    # Categoría de estudio
    path('categoria_estudio/<int:cate_id>/', views.categoria_estudio, name="categoria_estudio" ),
    # Eriquetas
    path('etiqueta/<int:etiqueta_id>/', views.etqtBiblio, name="categorias_biblio" ),
]