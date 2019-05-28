from django.contrib import admin
from .models import propuesta, grupo, repertorio


class propuestaAdmin(admin.ModelAdmin):
    readonly_fields=('created', 'updated')

class grupoAdmin(admin.ModelAdmin):
    readonly_fields=('created', 'updated')
    list_filter = ('created', 'updated')

class repertorioAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')
    date_hierarchy = 'created'
    list_display = ('titulo', 'created', 'updated')

admin.site.register(propuesta, propuestaAdmin)
admin.site.register(grupo, grupoAdmin)
admin.site.register(repertorio, repertorioAdmin)