from django.db import models
from supervision.models import Supervision

# Create your models here.
class Escuela(models.Model):
    nombre = models.CharField(max_length=20, blank=False, null=False)
    numero = models.IntegerField(blank=False, null=False)
    departamento = models.CharField(max_length=30, blank=True, null=True)
    supervision = models.ForeignKey(Supervision, on_delete=models.CASCADE, related_name='supervisiones', blank=True, null=True)

    def __str__(self):
        return self.nombre
    

    