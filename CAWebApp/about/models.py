from django.db import models
from django.utils.timezone import now
from django.contrib.auth.models import User


# Multiselectfield
from multiselectfield import MultiSelectField
# ckEditor
from ckeditor.fields import RichTextField



class Colaborador(models.Model):
    nombre = models.CharField(
        max_length=200, 
        verbose_name='Nombre',
    )
    created = models.DateField(
        auto_now_add=True
    )
    updated = models.DateTimeField(
        auto_now=True
    )

    class Meta():
        verbose_name = "Compañero"
        verbose_name_plural = 'Compañeros del Foro'
        ordering = ['created']

    def __str__(self):
        return str(self.nombre)


# Fecha jQuerry
class grupoForo(models.Model):
    nombre = models.ForeignKey(
        User, 
        verbose_name='Nombre', 
        blank =True, 
        null=True, 
        on_delete=models.PROTECT
    )

    puesto = models.CharField(
        max_length=200, 
        verbose_name='Puesto', 
        null=True
    )
    info = RichTextField(
        verbose_name='Información', 
        max_length=8000
    )
    imagenPerfil = models.ImageField(
        verbose_name="Imagen de perfil", 
        upload_to='nodos'
    )
    imagenBanner = models.ImageField(
        verbose_name="Imágen del Banner", 
        upload_to='nodos'
    )
    imagenExtra = models.ImageField(
        verbose_name="Imágen extra", 
        upload_to='nodos'
    )
    linkface = models.URLField(
        verbose_name='link', 
        null=True, 
        blank=True
    )
    created = models.DateField( auto_now_add=True, verbose_name='Fecha de Creación')
    updated = models.DateTimeField(auto_now=True, verbose_name='Fecha de Edición')

    class Meta:
        verbose_name = "Perfil"
        verbose_name_plural = 'Perfiles'
        ordering = ['-created']

    def __str__(self):
        return str(self.nombre)