from django.contrib import admin
from .models import preguntas

class preguntasAdmin(admin.ModelAdmin):
    readonly_fields=('created', 'updated')
    

admin.site.register(preguntas, preguntasAdmin)