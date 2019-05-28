# Generated by Django 2.0.2 on 2019-02-28 18:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('biblioteca', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='etiquetasBiblio',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Etiqueta')),
                ('created', models.DateField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('cat_estudio', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='categoriasEstudio', to='biblioteca.CategoryStudyBiblio', verbose_name='Categorias de estudio')),
                ('for_inline', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='biblioteca.etiquetasBiblio')),
            ],
            options={
                'verbose_name': 'Etiqueta Biblioteca',
                'verbose_name_plural': 'Etiquetas Biblioteca',
                'ordering': ['created'],
            },
        ),
    ]
