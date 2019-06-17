from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    # Path de Faqs
    path('', views.compañia, name='compañia'),
    path('actor/<int:act_id>/', views.compañia_bio, name="compañia_bio" ),
]