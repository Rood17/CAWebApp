from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    # Path de blog
    path('<category_id>/', views.Categorias, name="categorias"),
    path('', views.test, name='blog'),
]