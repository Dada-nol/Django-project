""" Ce fichier contient l'ensemble des fonctions pour afficher et créer un emprunt. """

from django.shortcuts import render
from bibliothecaire_app.Emprunt.forms import CreationEmprunt
from bibliothecaire_app.Media.models import Livre, Cd, Dvd
from bibliothecaire_app.Membre.models import Emprunteur
from bibliothecaire_app.Emprunt.models import EmpruntLivre, EmpruntDvd, EmpruntCd


def listeemprunt(request):
    """
    Méthode permettant de d'afficher la liste des emprunts.
    """
    emprunteurs = EmpruntLivre.objects.all()
    return render(request, 'Emprunt/Emprunt/listEmprunt.html',
                  {'emprunteurs': emprunteurs})


def empruntlivre(request, _id):
    """
    Méthode permettant de d'ajouter un emprunt et ainsi de lier un membre à un livre en base de données.
    """
    if request.method == 'POST':
        livre = Livre.objects.get(pk=_id)
        creationemprunt = CreationEmprunt(request.POST)
        if creationemprunt.is_valid():
            value = creationemprunt.cleaned_data['membre']
            membre = Emprunteur.objects.get(name=value)
            if livre.disponible and membre.NbEmprunt <= 2 and not membre.bloque:
                membre.NbEmprunt += 1
                membre.save()
                livre.disponible = False
                livre.save()
                membre.livres.add(livre)
            else:
                membre.bloque = True
                membre.save()
                return render(request, 'Emprunt/Erreur/Error_livre.html')
            emprunteurs = EmpruntLivre.objects.all()
            return render(request, 'Emprunt/Emprunt/listEmprunt.html',
                          {'emprunteurs': emprunteurs})
    else:
        creationemprunt = CreationEmprunt()
        return render(request,
                      'Emprunt/Emprunt/Empruntlivre.html',
                      {'creationemprunt': creationemprunt}
                      )


def empruntdvd(request, _id):
    """
    Méthode permettant de d'ajouter un emprunt et ainsi de lier un membre à un dvd en base de données.
    """
    if request.method == 'POST':
        dvd = Dvd.objects.get(pk=_id)
        creationemprunt = CreationEmprunt(request.POST)
        if creationemprunt.is_valid():
            value = creationemprunt.cleaned_data['membre']
            membre = Emprunteur.objects.get(name=value)
            if dvd.disponible and membre.NbEmprunt <= 2 and not membre.bloque:
                membre.NbEmprunt += 1
                membre.save()
                dvd.disponible = False
                dvd.save()
                membre.dvds.add(dvd)
            else:
                membre.bloque = True
                membre.save()
                return render(request, 'Emprunt/Erreur/Error_dvd.html')
            emprunteurs = EmpruntDvd.objects.all()
            return render(request, 'Emprunt/Emprunt/listEmprunt.html',
                          {'emprunteurs': emprunteurs})
    else:
        creationemprunt = CreationEmprunt()
        return render(request,
                      'Emprunt/Emprunt/Empruntdvd.html',
                      {'creationemprunt': creationemprunt}
                      )


def empruntcd(request, _id):
    """
    Méthode permettant de d'ajouter un emprunt et ainsi de lier un membre à un cd en base de données.
    """
    if request.method == 'POST':
        cd = Cd.objects.get(pk=_id)
        creationemprunt = CreationEmprunt(request.POST)
        if creationemprunt.is_valid():
            value = creationemprunt.cleaned_data['membre']
            membre = Emprunteur.objects.get(name=value)
            if cd.disponible and membre.NbEmprunt <= 2 and not membre.bloque:
                membre.NbEmprunt += 1
                membre.save()
                cd.disponible = False
                cd.save()
                membre.cds.add(cd)
            else:
                membre.bloque = True
                membre.save()
                return render(request, 'Emprunt/Erreur/Error_cd.html')
            emprunteurs = EmpruntCd.objects.all()
            return render(request, 'Emprunt/Emprunt/listEmprunt.html',
                          {'emprunteurs': emprunteurs})
    else:
        creationemprunt = CreationEmprunt()
        return render(request,
                      'Emprunt/Emprunt/Empruntcd.html',
                      {'creationemprunt': creationemprunt}
                      )
