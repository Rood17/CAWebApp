from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    # Path del Core
    path('', views.contact, name='contacto'),
]