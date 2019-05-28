from django.db import models

# Create your models here.
class Link(models.Model):
    key = models.SlugField(verbose_name="Nombre Clave", max_length=100, unique=True )
    name = models.CharField(verbose_name="Red Social", max_length=200)
    url = models.URLField(verbose_name="Enlace", null=True, blank=True, max_length=200)
    created = models.DateField(
        auto_now_add=True, 
        verbose_name='Fecha de Creación'
        )
    updated = models.DateTimeField(
        auto_now=True, 
        verbose_name='Fecha de Edición'
    )


    class Meta:
        verbose_name='Enlace'
        verbose_name_plural = 'Enlaces'
        ordering = ['created']

    def __str__(self):
        return self.name