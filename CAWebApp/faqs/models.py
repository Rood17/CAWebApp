from django.db import models
from django.utils.timezone import now
from django.contrib.auth.models import User


# Multiselectfield
from multiselectfield import MultiSelectField
# ckEditor
from ckeditor.fields import RichTextField

# Fecha jQuerry
class preguntas(models.Model):
    id_faqs = models.AutoField(primary_key=True)
    pregunta = RichTextField(
        verbose_name='Pregunta', 
        max_length=8000
    )
    respuesta = RichTextField(
        verbose_name='Respuesta', 
        max_length=8000
    )
    created = models.DateField( auto_now_add=True, verbose_name='Fecha de Creación')
    updated = models.DateTimeField(auto_now=True, verbose_name='Fecha de Edición')

    class Meta:
        verbose_name = "faq"
        verbose_name_plural = 'Faqs'
        ordering = ['-created']

    def __str__(self):
        return self.pregunta