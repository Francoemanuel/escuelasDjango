from django.db import models
from escuela.models import Escuela

# Create your models here.

class Persona(models.Model):
    documento = models.IntegerField(blank=False, null=False)
    nombre = models.CharField(max_length=20, blank=False, null=False)
    apellido = models.CharField(max_length=20, blank=False, null=False)
    localidad = models.CharField(max_length=30, blank=False, null=False)
    departamento = models.CharField(max_length=30, blank=False, null=False)

    def __str__(self):
        return f"{self.nombre} {self.apellido}"
    


class Alumno(Persona):
    nombre_padre = models.CharField(max_length=20, blank=True, null=True)
    apellido_padre = models.CharField(max_length=20, blank=True, null=True)
    nombre_madre = models.CharField(max_length=20, blank=True, null=True)
    apellido_madre = models.CharField(max_length=20, blank=True, null=True)
    nro_contacto = models.CharField(max_length=15, blank=True, null=True)
    escuela = models.ForeignKey(Escuela, on_delete=models.CASCADE, related_name='alumnos', null=True, blank=True)

    def __str__(self):
        return f"Alumno: {self.nombre} {self.apellido}"    