from django.db import models
from django.utils.timezone import now
from django.contrib.auth.models import User

# Multiselectfield
from multiselectfield import MultiSelectField
# ckEditor
from ckeditor.fields import RichTextField


# Línea del Tiempo
class imgGal(models.Model):
    # id = models.UUIDField(primary_key=True, default=uuid.uuid4, help_text="ID único para este libro particular en toda la biblioteca")
    titulo = models.CharField(
        max_length=200, 
        verbose_name='Título',
    )
    imagen = models.ImageField(
        verbose_name="", 
        upload_to='galeria'
    )
    # Selección de categoria
    CATE = (
        ('01', 'En Escena'),
        ('02', 'Nuestros Espacios'),
        ('03', 'Eventos'), 
    )
    presentacion = models.CharField(
        max_length=60,  
        choices=CATE, 
        default='01', 
        verbose_name='Categoria',
        help_text=''
    )
    year = models.IntegerField(
        verbose_name="Año", 
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
        verbose_name='Galería'
        verbose_name_plural = 'Galería de Imágenes'
        ordering = ['created']

    def __str__(self):
        return self.titulo