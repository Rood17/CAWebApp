from django.db import models
from django.utils.timezone import now
from django.contrib.auth.models import User

# Multiselectfield
from multiselectfield import MultiSelectField
# ckEditor
from ckeditor.fields import RichTextField



# Categorias del Blog.
class CategoryBlog(models.Model):
    categorias = models.CharField(
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
        verbose_name = "Categoria de etiqueta blog"
        verbose_name_plural = 'Categorias del Blog'
        ordering = ['created']

    def __str__(self):
        return self.categorias   


# Sistema de Etiquetas
# Categorias de Estudio del Blog
class CategoryStudyBlog(models.Model):
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
        verbose_name = "Categoria de estudio del blog"
        verbose_name_plural = 'Categorias de estudio del Blog'
        ordering = ['created']

    def __str__(self):
        return self.categoria 
# Etiquetas Blog
class etiquetasBlog(models.Model):
    cat_estudio = models.ForeignKey(
        CategoryStudyBlog, 
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
        verbose_name = "Etiqueta Blog"
        verbose_name_plural = 'Etiquetas Blog'
        ordering = ['created']

    def __str__(self):
        return self.name


# Entradas del Blog
class entradaBlog(models.Model):
    titulo = models.CharField(max_length=100, verbose_name='Título')
    
    # Imagen
    imagen = models.ImageField(
        verbose_name="Imagen principal", 
        upload_to='blog',
    )
    CAT = (
        ('01', 'Artículos'),
        ('02', 'Reseñas'),
        ('03', 'Entrevistas'),
        ('04', 'En Profundidad'),
        ('05', 'Noticias') 
    )
    categoria = models.CharField(
        max_length=60,  
        choices=CAT, 
        default='01', 
        verbose_name='Categoría',
        help_text=''
    )
       # Estado
    PUBLI = (
        ('01', 'Publicar'),
        ('02', 'No Publicar'), 
    )
    # Aquí debería ser ESTADO...
    donativo = models.CharField(
        max_length=60,  
        choices=PUBLI, 
        default='01', 
        verbose_name='Estado',
        help_text=''
    )

    contenido = RichTextField(
        verbose_name='Contenido', 
        max_length=180000
    )

    # Etiquetas Blog
    etiquetaBlog = models.ManyToManyField(
        'blog.etiquetasBlog',   
        verbose_name='Etiquetas',
        help_text='',
        related_name='get_etiquetaCart',
    )

    autor = models.ForeignKey(
        User, 
        verbose_name='Autor', 
        blank =True, 
        null=True, 
        on_delete=models.PROTECT
    )

    created = models.DateField( auto_now_add=True, verbose_name='Fecha de Creación')
    updated = models.DateTimeField(auto_now=True, verbose_name='Fecha de Edición')

    class Meta:
        verbose_name = "Entrada del Blog"
        verbose_name_plural = 'Entradas del Blog'
        ordering = ['-created']

    def __str__(self):
        return self.titulo