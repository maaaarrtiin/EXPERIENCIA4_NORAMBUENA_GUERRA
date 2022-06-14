# Generated by Django 4.0.5 on 2022-06-09 01:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('rut', models.CharField(max_length=10, primary_key=True, serialize=False, verbose_name='Rut')),
                ('nombre', models.CharField(max_length=20, verbose_name='Nombre')),
                ('telefono', models.IntegerField(verbose_name='Telefono')),
                ('correo', models.CharField(max_length=50, verbose_name='Correo')),
                ('edad', models.IntegerField(verbose_name='Correo')),
                ('raza_mascota', models.CharField(max_length=30, verbose_name='Raza Mascota')),
                ('cantidad_mascotas', models.IntegerField(verbose_name='Cantidad de Mascotas')),
            ],
        ),
    ]