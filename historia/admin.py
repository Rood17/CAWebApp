from django.contrib import admin
from .models import historia, bio
# Register your models here.

class historiaAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')
    date_hierarchy = 'created'
    search_fields = ('titulo', 'year','usuario__username')
    list_filter = ('year', 'usuario__username')
    list_display = ('titulo', 'created', 'updated')

class bioAdmin(admin.ModelAdmin):
    readonly_fields=('created', 'updated')
    list_display = ('nombre', 'puesto')
    list_filter = ('created', 'updated')

admin.site.register(historia, historiaAdmin)
admin.site.register(bio, bioAdmin)