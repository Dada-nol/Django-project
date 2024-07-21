""" Ce fichier contient l'ensemble une fonction pour afficher un média. """

from django.shortcuts import render
from bibliothecaire_app.Media.models import Livre, Dvd, Cd
from bibliothecaire_app.Media.models import JeuDePlateau as Jdp


def listemedia(request):
    """
    Méthode permettant de d'afficher la liste des médias.
    """
    livres = Livre.objects.all()
    dvds = Dvd.objects.all()
    cds = Cd.objects.all()
    jdps = Jdp.objects.all()
    return render(request, 'Media/list.html',
                  {'livres': livres, 'dvds': dvds, 'cds': cds, 'jdps': jdps})
