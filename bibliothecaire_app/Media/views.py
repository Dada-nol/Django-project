""" Ce fichier contient l'ensemble des fonctions pour afficher et créer un média. """

from django.shortcuts import render
from bibliothecaire_app.Media.forms import CreationMedia
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


def ajoutlivre(request):
    """
    Méthode permettant de d'ajouter un livre en base de données.
    """
    if request.method == 'POST':
        creationmedia = CreationMedia(request.POST)
        if creationmedia.is_valid():
            livre = Livre()
            livre.name = creationmedia.cleaned_data['name']
            livre.auteur = creationmedia.cleaned_data['créateur']
            livre.disponible = creationmedia.cleaned_data['disponible']
            livre.save()
            livres = Livre.objects.all()
            return render(request, 'Media/list.html',
                          {'livres': livres})
    else:
        creationmedia = CreationMedia()
        return render(request,
                      'Media/ajout-livre.html',
                      {'creationmedia': creationmedia}
                      )


def ajoutdvd(request):
    """
    Méthode permettant de d'ajouter un dvd en base de données.
    """
    if request.method == 'POST':
        creationmedia = CreationMedia(request.POST)
        if creationmedia.is_valid():
            dvd = Dvd()
            dvd.name = creationmedia.cleaned_data['name']
            dvd.realisateur = creationmedia.cleaned_data['créateur']
            dvd.disponible = creationmedia.cleaned_data['disponible']
            dvd.save()
            dvds = Dvd.objects.all()
            return render(request, 'Media/list.html',
                          {'dvds': dvds})
    else:
        creationmedia = CreationMedia()
        return render(request,
                      'Media/ajout-dvd.html',
                      {'creationmedia': creationmedia}
                      )


def ajoutcd(request):
    """
    Méthode permettant de d'ajouter un cd en base de données.
    """
    if request.method == 'POST':
        creationmedia = CreationMedia(request.POST)
        if creationmedia.is_valid():
            cd = Cd()
            cd.name = creationmedia.cleaned_data['name']
            cd.artiste = creationmedia.cleaned_data['créateur']
            cd.disponible = creationmedia.cleaned_data['disponible']
            cd.save()
            cds = Cd.objects.all()
            return render(request, 'Media/list.html',
                          {'cds': cds})
    else:
        creationmedia = CreationMedia()
        return render(request,
                      'Media/ajout-cd.html',
                      {'creationmedia': creationmedia}
                      )


def ajoutjdp(request):
    """
    Méthode permettant de d'ajouter un jeu de plateau en base de données.
    """
    if request.method == 'POST':
        creationmedia = CreationMedia(request.POST)
        if creationmedia.is_valid():
            jdp = Jdp()
            jdp.name = creationmedia.cleaned_data['name']
            jdp.createur = creationmedia.cleaned_data['créateur']
            jdp.save()
            jdps = Jdp.objects.all()
            return render(request, 'Media/list.html',
                          {'jdps': jdps})
    else:
        creationmedia = CreationMedia()
        return render(request,
                      'Media/ajout-jdp.html',
                      {'creationmedia': creationmedia}
                      )
