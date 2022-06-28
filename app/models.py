from django.db import models



# Create your models here.

class Cliente(models.Model):
    rut = models.CharField(primary_key=True, max_length=10, verbose_name='Rut')
    nombre = models.CharField(max_length=20, verbose_name='Nombre')
    telefono= models.IntegerField(verbose_name='Telefono')
    correo = models.CharField(max_length=50, verbose_name='Correo')
    direccion = models.CharField(max_length=50, verbose_name='Direccion')
    edad = models.IntegerField(verbose_name='Edad')
    cantidad_mascotas = models.IntegerField(verbose_name='Cantidad de Mascotas')


    def __str__(self):
        return self.rut


class Producto(models.Model):
    idprod = models.CharField(primary_key=True,max_length=10, verbose_name='Id Producto')
    image = models.ImageField(verbose_name="Imagen", upload_to="images")
    nombprod = models.CharField(max_length=50, verbose_name='Nombre producto')
    descripcion_prod= models.CharField(max_length=1000, verbose_name='Descripcion del producto')
    stock = models.IntegerField(verbose_name='Stock del producto')


    def __str__(self):
        return self.idprod