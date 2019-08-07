from django.contrib import admin
from .models import Presentaciones, Obra, diaSemana, fechaCalendario, etiquetasCar, CategoryStudy
from .forms import fechaCalendarioForm, AutocompleteEtiquetasForm

# Fecha jQuerry 
class TestInline(admin.TabularInline):
    # form = fechaCalendarioForm
    model = fechaCalendario
    fk_name = 'for_inline'  
class fechaCalendarioAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')
    fields = ('fechaCa', )
    inlines = [TestInline]


# Etiquetas ManytoMany
class CategoryStudyAdmin(admin.ModelAdmin):
    readonly_fields=('created', 'updated')
    list_display = ('categoria_estudio', 'created', 'updated')
    list_filter = ('categoria_estudio', 'updated')
class TestInlineCart(admin.TabularInline):
    # form = AutocompleteEtiquetasForm
    model = etiquetasCar
    fk_name = 'for_inline'  
class etiquetasCarAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')
    fields = ('name', 'cat_estudio')
    inlines = [TestInlineCart]


# Día de la Sem ForeignKey
class diaSemanaAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')
    

# Obra Títulos
class ObraAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')


# Cartelera - Función
class PresentacionesAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated', 'usuario')
    date_hierarchy = 'created'
    search_fields = ('titulo', 'usuario__username')
    readonly_fields = ('created', 'updated')
    list_filter = ('presentacion', 'status')
    list_display = ('titulo', 'presentacion','status', 'created', 'updated')
    fields = ['titulo','presentacion','status','Cartel','imagenPortada',
              ('diaSem', 'hora'), 'fechaCal', 'donativo', 'sinopsis', 'elenco',
                'Agrupacion', 'etiquetasCartelera', 'publico', 'duracion', 'grupoLink',
                ]
    # form = AutocompleteEtiquetasForm




admin.site.register(Presentaciones, PresentacionesAdmin)
admin.site.register(diaSemana, diaSemanaAdmin)
admin.site.register(fechaCalendario, fechaCalendarioAdmin)
admin.site.register(etiquetasCar, etiquetasCarAdmin)
admin.site.register(CategoryStudy, CategoryStudyAdmin)
admin.site.register(Obra, ObraAdmin)

def autor(self):
        return ([ Obra.autor for Obra in Obra.objects.all()])
        autor.short_description = 'Autor'