# Generated by Django 4.0.5 on 2022-06-09 03:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_remove_cliente_raza_mascota_alter_cliente_edad_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cliente',
            name='rut',
            field=models.CharField(max_length=10, primary_key=True, serialize=False, verbose_name='Rut'),
        ),
    ]
