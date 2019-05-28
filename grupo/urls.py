from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    # Path de Faqs
    path('', views.compañia, name='compañia'),

]