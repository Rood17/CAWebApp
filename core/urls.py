from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    # Path del Core
    path('', views.index, name='index'),
    path('base/', views.base, name='base'),
    path('foro/', views.foro, name='foro'),
    path('convocatorias/', views.convocatorias, name='convocatorias'),
    path('rentas/', views.rentas, name='rentas'),
]