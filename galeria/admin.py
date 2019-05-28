from django.contrib import admin
from .models import imgGal
# Register your models here.

class imgGalAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')
    date_hierarchy = 'created'
    list_filter = ('year', 'presentacion')
    list_display = ('titulo','presentacion', 'created', 'updated')

admin.site.register( imgGal, imgGalAdmin)