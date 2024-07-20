""" Fichier permettant le peuplement de la base de données avec le model EmpruntLivre, EmpruntDvd, EmpruntCd."""

from django.db import models
from datetime import date
from bibliothecaire_app.Membre.models import Emprunteur
from bibliothecaire_app.Media.models import Livre, Dvd, Cd


class Emprunt(models.Model):
    membre = models.ForeignKey(Emprunteur, on_delete=models.CASCADE)
    dateEmprunt = models.fields.DateField(default=date.today)
    dateEmprunt_max = models.fields.DateField(default=date.today().replace(day=date.today().day + 7))

    class Meta:
        """ Ce model est le parent des models suivant mais n'apparait pas en base de données."""
        abstract = True


class EmpruntLivre(Emprunt):
    objects = models.Manager()
    livre = models.ForeignKey(Livre, on_delete=models.CASCADE)


class EmpruntCd(Emprunt):
    objects = models.Manager()
    cd = models.ForeignKey(Cd, on_delete=models.CASCADE)


class EmpruntDvd(Emprunt):
    objects = models.Manager()
    dvd = models.ForeignKey(Dvd, on_delete=models.CASCADE)
