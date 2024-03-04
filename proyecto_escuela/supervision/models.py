from django.db import models

# Create your models here.

class Supervision(models.Model):
    responsable = models.CharField(max_length=150, blank=False, null=False)
    nombre = models.CharField(max_length=150, blank=False, null=False)
    email = models.EmailField(max_length=100, blank= False, null=False)

    def __str__(self):
        return f"Supervisión de {self.nombre}"