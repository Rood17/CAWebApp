"""CAWebApp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings


urlpatterns = [
    # Path de About
    path('acerca/', include('about.urls')),
    # Path de Biblioteca
    path('biblioteca/', include('biblioteca.urls')),
    # Path de Blog
    path('blog/', include('blog.urls')),
    # Path de Cartelera
    path('cartelera/', include('cartelera.urls')),
    # Path del Core
    path('', include('core.urls')),
    # Path de Faqs
    path('faqs/', include('faqs.urls')),
    # Path Galería
    path('galeria/', include('galeria.urls')),
    # Path de Grupo
    path('compañia/', include('grupo.urls')),
    # Path de Historia
    path('historia/', include('historia.urls')),
    # Path del contacto
    path('contacto/', include('contacto.urls')),
    # Path del admin
    path('admin/', admin.site.urls),
    
]

if settings.DEBUG:
    from django.conf.urls.static import static
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


