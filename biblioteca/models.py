from django.db import models
from django.utils.timezone import now
from django.contrib.auth.models import User
from django.db.models import Q


# Multiselectfield
from multiselectfield import MultiSelectField
# ckEditor
from ckeditor.fields import RichTextField

# Sistema de Etiquetas
# Categorias de Estudio del Blog
class CategoryStudyBiblio(models.Model):
    categoria = models.CharField(
        max_length=200, 
        verbose_name="Categoria"
    )
    created = models.DateField(
        auto_now_add=True
    )
    updated = models.DateTimeField(
        auto_now=True
    )

    class Meta():
        verbose_name = "Categoria de estudio"
        verbose_name_plural = 'Categorias de estudio'
        ordering = ['created']

    def __str__(self):
        return self.categoria 

# Etiquetas Biblioteca
class etiquetasBiblio(models.Model):
    cat_estudio = models.ForeignKey(
        CategoryStudyBiblio, 
        on_delete=models.CASCADE, 
        verbose_name='Categorias de estudio', 
        related_name='categoriasEstudio',
    )
    name = models.CharField(
        max_length=100,
        verbose_name='Etiqueta',
        help_text='',
        
    )
    for_inline = models.ForeignKey(
        'self',
        blank=True,
        null=True,
        on_delete=models.CASCADE, 
    )
    created = models.DateField(
        auto_now_add=True
    )
    updated = models.DateTimeField(
        auto_now=True
    )

    class Meta():
        verbose_name = "Etiqueta Biblioteca"
        verbose_name_plural = 'Etiquetas Biblioteca'
        ordering = ['created']

    def __str__(self):
        return self.name

# Book Search
class BookManager(models.Manager):
    def search(self, query):
        qs = self.get_queryset()

        if query is not None:
            or_lookup = (Q(titulo__icontains=query) | 
                         Q(autor__icontains=query) |
                         Q(editorial__icontains=query) |
                        Q(categorias__name__icontains=query)
                        )
            qs = qs.filter(or_lookup).distinct() # distinct() is often necessary with Q lookups
        return qs

# Book
class Book(models.Model):
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
    descripcion = RichTextField(
        verbose_name='Escribe aquí una breve descripción del libro', 
        max_length=18000
    )
    imagen = models.ImageField(
        verbose_name="portada del libro", 
        upload_to='nodos'
    )
    isbn = models.FloatField(
        verbose_name='Introduce el ISBN', 
        blank=True, null=True ,
        max_length=13, 
        help_text='13 Character <a href="https://www.isbn-international.org/content/what-isbn">ISBN number</a>'
    )
    editorial = models.CharField(
        max_length=200, 
        verbose_name='Editorial',
        null=True
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

    # Categorías de Estudio

    cate_estudio = models.ManyToManyField(
        'biblioteca.CategoryStudyBiblio',   
        verbose_name='Categorías de estudio',
        help_text='Seleccione las categorías de estudio que contine el libro.',
        related_name='get_cat_estudy'
    )

    categorias = models.ManyToManyField(
        'biblioteca.etiquetasBiblio', 
        verbose_name='Etiquetas', 
        related_name='get_nodos'
    )
    


    # Mapas
    pais = models.CharField(
        max_length=20, 
        default='México', 
        verbose_name='País y/o Edo'
    )

    created = models.DateField(
        auto_now_add=True, 
        verbose_name='Fecha de Creación'
        )
    updated = models.DateTimeField(
        auto_now=True, 
        verbose_name='Fecha de Edición'
    )
    objects = BookManager()


    class Meta:
        verbose_name='Libro'
        verbose_name_plural = 'Libros'
        ordering = ['created']

    def __str__(self):
        return self.titulo





