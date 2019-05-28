# Generated by Django 2.0.2 on 2019-05-21 21:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('social', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='link',
            name='name',
            field=models.CharField(default=True, max_length=200, verbose_name='Red Social'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='link',
            name='url',
            field=models.URLField(blank=True, null=True, verbose_name='Enlace'),
        ),
    ]
