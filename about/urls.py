from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    # Path de about
    path('', views.perfiles, name='acerca'),
    path('compañero/<int:colaborador_id>/', views.AboutBio, name='acerca-bio'),
]