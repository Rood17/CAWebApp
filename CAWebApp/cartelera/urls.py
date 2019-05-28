from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    # Path de cartelera
    path('', views.cartelera, name='cartelera'),
    path('obra/<int:obra_id>/', views.CarteleraBio, name="obra"),

]