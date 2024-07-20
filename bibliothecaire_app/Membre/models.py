""" Fichier permettant le peuplement de la base de données avec le model Emprunteur."""

from django.db import models


class Emprunteur(models.Model):
    objects = models.Manager()
    name = models.fields.CharField(max_length=150)
    NbEmprunt = models.fields.IntegerField(default=0)
    bloque = models.fields.BooleanField(default=False)

    def __str__(self):
        return self.name
