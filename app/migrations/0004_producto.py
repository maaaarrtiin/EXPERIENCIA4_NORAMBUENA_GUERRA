# Generated by Django 4.0.5 on 2022-06-09 20:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_alter_cliente_rut'),
    ]

    operations = [
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('image', models.ImageField(upload_to='app', verbose_name='Imagen')),
                ('idprod', models.IntegerField(primary_key=True, serialize=False, verbose_name='Id Producto')),
                ('nombprod', models.CharField(max_length=50, verbose_name='Nombre producto')),
                ('descripcion_prod', models.CharField(max_length=1000, verbose_name='Descripcion del producto')),
                ('stock', models.IntegerField(verbose_name='Stock del producto')),
            ],
        ),
    ]
