from django.db import models
from django.utils import timezone

# Create your models here.
class Biblioteca(models.Model):
    nombre = models.CharField()
    direccion = models.TextField()


class Autor(models.Model):
    nombre = models.CharField()
    apellidos = models.CharField()
    edad = models.IntegerField()



class Libro(models.Model):
    IDIOMAS = [
        {"ES", "Español"},
        {"EN", "English"},
        {"FR", "Frances"},
        {"IT", "Italiano"},
    ]

    nombre = models.CharField()
    tipo = models.CharField(
        max_length=2,
        choices=IDIOMAS,
        default="ES",
    )
descripcion = models.TextField()
fecha_publicacion = models.DateField()
biblioteca = models.ForeignKey(Biblioteca, on_delete = models.CASCADE)
autores = models.ManyToManyField(Autor)


class Cliente(models.Model):
    nombre = models.CharField()
    email = models.CharField()
    puntos = models.FloatField()
    libros = models.ManyToManyField(Libro, through='Prestamos')

class Prestamos(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    libro = models.ForeignKey(Libro, on_delete=models.CASCADE)
    fecha_prestamo = models.DateTimeField(default=timezone.now)

class DatosCliente(models.Model):
    cliente = models.OneToOneField(Cliente, 
                            on_delete = models.CASCADE)
    direccion = models.TextField()
    gustos = models.TextField()
    telefono = models.CharField()