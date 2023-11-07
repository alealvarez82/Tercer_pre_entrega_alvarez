from django.db import models

class Instrumentos(models.Model):
    nombre = models.CharField(max_length=64)
    tipo = models.CharField(max_length=64)

class Musicos(models.Model):
    apellido = models.CharField(max_length=256)
    nombre = models.CharField(max_length=256)
    fecha_nacimiento = models.DateField(null=True)
    instrumento = models.CharField(max_length=256)

class Notas(models.Model):
    nota_de_interes = models.CharField(max_length=25600)    