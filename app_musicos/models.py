from django.db import models

class Instrumentos(models.Model):
    nombre = models.CharField(max_length=64)
    tipo = models.CharField(max_length=64)

class Musicos(models.Model):
    nombre = models.CharField(max_length=256)
    instrumento = models.CharField(max_length=256)

class Notas(models.Model):
    nota_de_interes = models.CharField(max_length=25600)    