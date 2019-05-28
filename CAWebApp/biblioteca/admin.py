from django.contrib import admin
from .models import CategoryStudyBiblio, etiquetasBiblio, Book

# Etiquetas
class CategoryStudyBlogAdmin(admin.ModelAdmin):
    readonly_fields=('created', 'updated')
    list_display = ('categoria', 'created', 'updated')
    list_filter = ('categoria', 'updated')
class TestInlineBiblio(admin.TabularInline):
    # form = AutocompleteBlog
    model = etiquetasBiblio
    fk_name = 'for_inline'  
class etiquetasBiblioAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')
    list_display = ('name', 'cat_estudio','created', 'updated')
    fields = ('name', 'cat_estudio')
    inlines = [TestInlineBiblio]

# Book
class BookAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')
    date_hierarchy = 'created'
    search_fields = ('titulo', 'etiquetaBiblio__name','usuario__username')
    readonly_fields = ('created', 'updated')
    list_filter = ('categorias__cat_estudio', 'usuario__username')
    list_display = ('titulo', 'created', 'updated')


admin.site.register(CategoryStudyBiblio, CategoryStudyBlogAdmin)
admin.site.register(etiquetasBiblio, etiquetasBiblioAdmin)
admin.site.register(Book, BookAdmin)