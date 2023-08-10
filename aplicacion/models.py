from django.db import models


# Create your models here.
class Receta(models.Model):
    nombre = models.CharField(max_length=50)
    ingredientes = models.CharField(max_length=200)
    tiempo = models.IntegerField()
    dificultad = models.IntegerField()

    def __str__(self):
        return self.nombre


class Cocinero(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    edad = models.IntegerField()
    especialidad = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre + " " + self.apellido


class Restaurante(models.Model):
    nombre = models.CharField(max_length=50)
    direccion = models.CharField(max_length=50)
    telefono = models.CharField(max_length=50)
    categoria = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre


class Proveedor(models.Model):
    nombre = models.CharField(max_length=50)
    telefono = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    producto = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre + " - " + self.producto
