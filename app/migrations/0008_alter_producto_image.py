# Generated by Django 4.0.5 on 2022-06-09 23:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0007_alter_producto_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='producto',
            name='image',
            field=models.ImageField(upload_to='app', verbose_name='Imagen'),
        ),
    ]