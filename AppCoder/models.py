import email
from pyexpat import model
from django.db import models

# Create your models here.
class Familia(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    edad = models.IntegerField()

class Momento(models.Model):
    dia = models.DateField()
    hora = models.TimeField()