from django.db import models

# Create your models here.
class Faixas(models.Model):
    arte_marcial = models.CharField(max_length=25)
    cor = models.CharField(max_length=25)
    requer = models.CharField(max_length=50)


class Comidas(models.Model):
    nome = models.CharField(max_length=25)
    nutriente = models.CharField(max_length=25)
    cor = models.CharField(max_length=25)


class Finalizacao(models.Model):
    arte_marcial = models.CharField(max_length=25)
    tipo = models.CharField(max_length=50)
    pontos = models.IntegerField()
