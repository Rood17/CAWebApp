from django.db import models
from django.utils.timezone import now
from django.contrib.auth.models import User

# Multiselectfield
from multiselectfield import MultiSelectField
# ckEditor
from ckeditor.fields import RichTextField


# Línea del Tiempo
class historia(models.Model):
    # id = models.UUIDField(primary_key=True, default=uuid.uuid4, help_text="ID único para este libro particular en toda la biblioteca")
    titulo = models.CharField(
        max_length=200, 
        verbose_name='Título',
    )
    descripcion = RichTextField(
        verbose_name='Escribe aquí una breve descripción del libro', 
        max_length=18000
    )
    imagen = models.ImageField(
        verbose_name="portada del libro", 
        upload_to='historia'
    )
    year = models.IntegerField(
        verbose_name="Año de edición", 
        blank=True, 
        null=True
    )
    usuario = models.ForeignKey(User, 
        verbose_name='Usuario', 
        blank =True, 
        null=True, 
        on_delete=models.PROTECT
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
        verbose_name='Línea del Tiempo'
        verbose_name_plural = 'Línea del Tiempo'
        ordering = ['created']

    def __str__(self):
        return self.titulo


class bio(models.Model):
    nombre = models.CharField(
        max_length=200, 
        verbose_name='Nombre',
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
    linkface = models.URLField(
        verbose_name='link', 
        null=True, 
        blank=True
    )
    created = models.DateField( auto_now_add=True, verbose_name='Fecha de Creación')
    updated = models.DateTimeField(auto_now=True, verbose_name='Fecha de Edición')

    class Meta:
        verbose_name = "Biografía"
        verbose_name_plural = 'Biografías'
        ordering = ['-created']

    def __str__(self):
        return self.nombre