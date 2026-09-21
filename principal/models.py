from django.db import models


class TipoIA(models.Model):
    nombre = models.CharField(max_length=100)
    definicion = models.TextField()

    def __str__(self):
        return self.nombre


class Concepto(models.Model):
    nombre = models.CharField(max_length=100)
    definicion = models.TextField()

    def __str__(self):
        return self.nombre


class Infografia(models.Model):
    titulo = models.CharField(max_length=150)
    descripcion = models.TextField(blank=True)
    imagen = models.ImageField(upload_to='infografias/')

    def __str__(self):
        return self.titulo
