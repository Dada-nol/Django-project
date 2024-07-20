""" Fichier permettant le peuplement de la base de données avec le model Livre, Cd, Dvd et Jeu de plateau."""

from django.db import models
from bibliothecaire_app.Membre.models import Emprunteur


class Media(models.Model):
    objects = models.Manager()
    name = models.fields.CharField(max_length=150)
    disponible = models.fields.BooleanField(default=True)

    class Meta:
        """ Ce model est le parent des models suivant mais n'apparait pas en base de données."""
        abstract = True


class Livre(Media):
    auteur = models.fields.CharField(max_length=150)
    membres = models.ManyToManyField(Emprunteur, through="EmpruntLivre", related_name="livres")


class Dvd(Media):
    realisateur = models.fields.CharField(max_length=150)
    membres = models.ManyToManyField(Emprunteur, through="EmpruntDvd", related_name="dvds")


class Cd(Media):
    artiste = models.fields.CharField(max_length=150)
    membres = models.ManyToManyField(Emprunteur, through="EmpruntCd", related_name="cds")


class JeuDePlateau(models.Model):
    objects = models.Manager()
    name = models.fields.CharField(max_length=150)
    createur = models.fields.CharField(max_length=150)
