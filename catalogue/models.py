from django.db import models

# Create your models here.

class Director(models.Model):
    nombre = models.CharField(max_length=64, help_text='Nombre del director de cine')

    def __str__(self) -> str:
        return self.nombre

class Pelicula(models.Model):
    titulo = models.CharField(max_length=64, help_text='Nombre de la película')
    director = models.ForeignKey('Director', on_delete=models.SET_NULL, null=True)
    descripcion = models.TextField(max_length=500, help_text='Descripción de la película')

    def __str__(self) -> str:
        return self.titulo


