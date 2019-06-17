from django.contrib import admin
from .models import CategoryBlog, CategoryStudyBlog, etiquetasBlog, entradaBlog

# Categorías del Blog
class CategoryBlogAdmin(admin.ModelAdmin):
    readonly_fields=('created', 'updated')
    list_display = ('categorias', 'created', 'updated')
    list_filter = ('categorias', 'updated')


# Sistema de Etiquetas
# Categorías de Estudio del Blog
class CategoryStudyBlogAdmin(admin.ModelAdmin):
    readonly_fields=('created', 'updated')
    list_display = ('categoria', 'created', 'updated')
    list_filter = ('categoria', 'updated')
class TestInlineBlog(admin.TabularInline):
    # form = AutocompleteBlog
    model = etiquetasBlog
    fk_name = 'for_inline'  
class etiquetasBlogAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')
    list_display = ('name', 'cat_estudio','created', 'updated')
    fields = ('name', 'cat_estudio')
    inlines = [TestInlineBlog]


# Entradas del Blog
class entradaBlogAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')
    date_hierarchy = 'created'
    search_fields = ('titulo', 'etiquetaBlog__name','autor__username')
    readonly_fields = ('created', 'updated')
    list_filter = ('donativo','etiquetaBlog__cat_estudio', 'autor__username')
    list_display = ('titulo', 'donativo', 'created', 'updated')
    


admin.site.register(CategoryBlog, CategoryBlogAdmin)
admin.site.register(CategoryStudyBlog, CategoryStudyBlogAdmin)
admin.site.register(etiquetasBlog, etiquetasBlogAdmin)
admin.site.register(entradaBlog, entradaBlogAdmin)