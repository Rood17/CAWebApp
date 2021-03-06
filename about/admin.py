from django.contrib import admin
from .models import grupoForo, Colaborador


class grupoForoAdmin(admin.ModelAdmin):
    readonly_fields=('created', 'updated')
    list_display = ('nombre', 'puesto')
    list_filter = ('created', 'updated')


admin.site.register(grupoForo, grupoForoAdmin)
