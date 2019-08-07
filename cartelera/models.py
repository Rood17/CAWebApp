from django.db import models
from django.utils.timezone import now
from django.contrib.auth.models import User

# Multiselectfield
from multiselectfield import MultiSelectField
# ckEditor
from ckeditor.fields import RichTextField



# Fechas jQuerry
class fechaCalendario(models.Model):
    fechaCa = models.CharField(
        max_length=2,
        verbose_name='Introduzca el/los días de función. ',
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
        verbose_name = "Fecha de función"
        verbose_name_plural = 'Fecha de funciones'
        ordering = ['created']

    def __str__(self):
        return self.fechaCa

class diaSemana(models.Model):
    diaSem = models.CharField(
        max_length=2, 
        verbose_name="Día de la Semana"
    )
    created = models.DateField(
        auto_now_add=True
    )
    updated = models.DateTimeField(
        auto_now=True
    )

    class Meta():
        verbose_name = "Día de la Semana"
        verbose_name_plural = 'Días de la Semana'
        ordering = ['created']

    def __str__(self):
        return self.diaSem


    # Etiquetas Cartelera

# Sistema Etiquetas Cartelera
class CategoryStudy(models.Model):
    categoria_estudio = models.CharField(
        max_length=200, 
        verbose_name="Categoria de estudio"
    )
    created = models.DateField(
        auto_now_add=True
    )
    updated = models.DateTimeField(
        auto_now=True
    )

    class Meta():
        verbose_name = "Categoria de etiqueta cartelera"
        verbose_name_plural = 'Categorias de estudio etiquetas de cartelera'
        ordering = ['created']

    def __str__(self):
        return self.categoria_estudio   
class etiquetasCar(models.Model):
    cat_estudio = models.ForeignKey(
        CategoryStudy, 
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
        verbose_name = "Etiqueta Cartelera"
        verbose_name_plural = 'Etiqueta Cartelera'
        ordering = ['created']

    def __str__(self):
        return self.name

# Foreign Key Titulo
class Obra(models.Model):
    titulo = models.CharField(max_length=100, verbose_name='Título')
    autor = models.CharField(max_length=50, null=True, blank=True, 
                                verbose_name='Autor', 
                                help_text="")
    director = models.CharField(max_length=50, null=True, blank=True, 
                                verbose_name='Director', 
                                help_text='')
    autorydir = models.CharField(
        max_length=50, null=True, 
        blank=True, verbose_name='Autor y Director', 
        help_text='Si es Autor y Director dejar en blanco los espacios de la parte superior y solo llenar este.')
    created = models.DateField(
        default=now
    )
    updated = models.DateTimeField(
        auto_now=True
    )

    class Meta():
        verbose_name = "Obra"
        verbose_name_plural = 'Títulos y Autores'
        ordering = ['created']

    def __str__(self):
        return str(self.titulo)


# Funciones
class Presentaciones(models.Model):
    titulo = models.ForeignKey(Obra,on_delete=models.CASCADE, verbose_name='Título')
    # titulo = models.CharField(max_length=100, verbose_name='Título')

    # Selección de tipo de presentación
    PRESEN = (
        ('01', 'Programación Normal'),
        ('02', 'Presentación Especial'), 
    )
    presentacion = models.CharField(
        max_length=60,  
        choices=PRESEN, 
        default='01', 
        verbose_name='Tipo de presentacion',
        help_text='Seleccione el tipo de presentación'
    )
    STAT = (
        ('01', 'En Temporada'),
        ('02', 'Fuera de Cartelera'), 
    )
    status = models.CharField(
        max_length=60,  
        choices=STAT, 
        default='02', 
        verbose_name='Status de la obra',
        help_text='Seleccione si la obra aparece en Cartelera'
    )
    # Imagen
    Cartel = models.ImageField(
        verbose_name="Cartel de la Obra", 
        upload_to='cartelera',
    )
    imagenPortada = models.ImageField(
        verbose_name="Foto de portada", 
        upload_to='cartelera'
    )

    # Fechas
    diaSem = models.ManyToManyField(
        'cartelera.diaSemana',   
        verbose_name='Día(s) de la semana. ',
        help_text='Día(s) de la semana que se presenta la obra.',
        related_name='get_diaSem',
    )
    hora = models.CharField(
        max_length=5,
        verbose_name="Hora",
        help_text='Introduzca el horario de la presentación, ej: "21:00".',
        default="21:00",
    )
        # Fecha para el calendario de jQuerry
    fechaCal = models.ManyToManyField(
        'cartelera.fechaCalendario',   
        verbose_name='Días',
        help_text='Seleccione los días que se presentará la obra.',
        related_name='get_fechaCal',
    )
     


       # Donativo
    DONA = (
        ('01', 'Donativo'),
        ('02', 'Precio'), 
    )
    donativo = models.CharField(
        max_length=60,  
        choices=DONA, 
        default='01', 
        verbose_name='Costo',
        help_text=''
    )
    

    sinopsis = RichTextField(
        verbose_name='Sinopsis', 
        max_length=8000
    )
    elenco = RichTextField(
        verbose_name='Reparto', 
        max_length=8000
    )

    # Etiquetas Cartelera
    etiquetasCartelera = models.ManyToManyField(
        'cartelera.etiquetasCar',   
        verbose_name='Género y demás clasificaciones',
        help_text='Etiquetas para filtros',
        related_name='get_etiquetaCart',
    )

    Agrupacion = models.CharField(max_length=100,default=None, verbose_name='Nombre de la Agrupación')      

    PUBLICO_CHOICES =(
        ('01', 'Para todo público'),
        ('02', 'Adolecentes y adultos'),
        ('03', 'Función para niños'),
        ('04', 'Sin definir'),
    )
    publico = models.CharField(
        max_length=2,  
        choices=PUBLICO_CHOICES, 
        default='01', 
        verbose_name='Público',
        help_text=''
    )
    duracion = models.CharField(
        default=None,
        max_length=100, 
        verbose_name='Duración',
        help_text="Introduzca la duración de la presentación."
    )

    grupoLink = models.URLField(verbose_name="Facebook del Grupo", null=True, blank=True)
    usuario = models.ForeignKey(
        User, 
        verbose_name='Usuario', 
        blank =True, 
        null=True, 
        on_delete=models.PROTECT,
        default=User
    )



    created = models.DateField( auto_now_add=True, verbose_name='Fecha de Creación')
    updated = models.DateTimeField(auto_now=True, verbose_name='Fecha de Edición')

    class Meta:
        verbose_name = "Función"
        verbose_name_plural = 'Funciones'
        ordering = ['-created']

    def __str__(self):
        return str(self.titulo)
    
