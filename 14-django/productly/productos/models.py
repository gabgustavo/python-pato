from django.db import models
from django.utils import timezone

# Create your models here.


class Categoria(models.Model):
    nombre = models.CharField(max_length=255)

    # redefinir str
    def __str__(self):
        return self.nombre


class Producto(models.Model):
    nombre = models.CharField(max_length=255)
    stock = models.IntegerField()
    puntaje = models.FloatField()

    # CASCADE: elimina el producto
    # PROTECT: lanza un error si hay relaciones
    # RESTRICT: solo elimina si no hay relaciones
    # SET_NULL: actualiza al valor NULL
    # SET_DEFAULT: asigna un valor por defecto
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)

    # actualizar el modelo
    creado_en = models.DateTimeField(default=timezone.now)

    # redefinir str

    def __str__(self):
        return self.nombre
