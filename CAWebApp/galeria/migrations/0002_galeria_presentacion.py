# Generated by Django 2.0.2 on 2019-02-28 19:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('galeria', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='galeria',
            name='presentacion',
            field=models.CharField(choices=[('01', 'En Escena'), ('02', 'Nuestros Espacios'), ('03', 'Eventos')], default='01', max_length=60, verbose_name='Categoria'),
        ),
    ]
