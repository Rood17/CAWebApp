# Generated by Django 2.0.2 on 2019-02-28 19:09

import ckeditor.fields
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='bio',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=200, verbose_name='Nombre')),
                ('puesto', models.CharField(max_length=200, null=True, verbose_name='Puesto')),
                ('info', ckeditor.fields.RichTextField(max_length=8000, verbose_name='Información')),
                ('imagenPerfil', models.ImageField(upload_to='nodos', verbose_name='Imagen de perfil')),
                ('linkface', models.URLField(blank=True, null=True, verbose_name='link')),
                ('created', models.DateField(auto_now_add=True, verbose_name='Fecha de Creación')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Fecha de Edición')),
            ],
            options={
                'verbose_name': 'Biografía',
                'verbose_name_plural': 'Biografías',
                'ordering': ['-created'],
            },
        ),
        migrations.CreateModel(
            name='historia',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=200, verbose_name='Título')),
                ('descripcion', ckeditor.fields.RichTextField(max_length=18000, verbose_name='Escribe aquí una breve descripción del libro')),
                ('imagen', models.ImageField(upload_to='nodos', verbose_name='portada del libro')),
                ('year', models.IntegerField(blank=True, null=True, verbose_name='Año de edición')),
                ('created', models.DateField(auto_now_add=True, verbose_name='Fecha de Creación')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Fecha de Edición')),
                ('usuario', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL, verbose_name='Usuario')),
            ],
            options={
                'verbose_name': 'Libro',
                'verbose_name_plural': 'Libros',
                'ordering': ['created'],
            },
        ),
    ]