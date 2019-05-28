from django.db import models
from django.utils.timezone import now
from django.contrib.auth.models import User

# Multiselectfield
from multiselectfield import MultiSelectField
# ckEditor
from ckeditor.fields import RichTextField


# Propuesta
class propuesta(models.Model):
    propuesta = RichTextField(
        verbose_name='Propuesta del Grupo', 
        max_length=18000
    )
    created = models.DateField(
        auto_now_add=True, 
        verbose_name='Fecha de Creación'
        )
    updated = models.DateTimeField(
        auto_now=True, 
        verbose_name='Fecha de Edición'
    )
    class Meta:
        verbose_name='Propuesta del Grupo'
        verbose_name_plural = 'Propuesta del Grupo'
        ordering = ['created']

    def __str__(self):
        return self.propuesta

# Galería y Bio
class grupo(models.Model):
    nombre = models.CharField(
        max_length=200, 
        verbose_name='Nombre',
    )
    info = RichTextField(
        verbose_name='Información', 
        max_length=8000
    )
    imagenPerfil = models.ImageField(
        verbose_name="Imagen de perfil", 
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
        verbose_name = "Compañía"
        verbose_name_plural = 'Compañía'
        ordering = ['-created']

    def __str__(self):
        return self.nombre


# Repertorio
class repertorio(models.Model):
    # id = models.UUIDField(primary_key=True, default=uuid.uuid4, help_text="ID único para este libro particular en toda la biblioteca")
    titulo = models.CharField(
        max_length=200, 
        verbose_name='Título',
    )
    autor = models.CharField(
        max_length=200, 
        verbose_name='Autor', 
        null=True
    )
    director = models.CharField(
        max_length=200, 
        verbose_name='Director', 
        null=True
    )
    descripcion = RichTextField(
        verbose_name='Descripción', 
        max_length=18000
    )
    imagen = models.ImageField(
        verbose_name="Imagen", 
        upload_to='grupo'
    )
    usuario = models.ForeignKey(User, 
        verbose_name='Usuario', 
        blank =True, 
        null=True, 
        on_delete=models.PROTECT
    )

    created = models.DateField( auto_now_add=True, verbose_name='Fecha de Creación')
    updated = models.DateTimeField(auto_now=True, verbose_name='Fecha de Edición')

    class Meta:
        verbose_name='Repertorio'
        verbose_name_plural = 'Repertorio'
        ordering = ['created']

    def __str__(self):
        return self.titulo
