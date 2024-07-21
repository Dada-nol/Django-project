""" Ce fichier contient l'ensemble des fonctions pour afficher et créer et supprimer un emprunt. """

from django.shortcuts import render
from bibliothecaire_app.Emprunt.forms import CreationEmprunt, RetourEmprunt
from bibliothecaire_app.Media.models import Livre, Cd, Dvd
from bibliothecaire_app.Membre.models import Emprunteur
from bibliothecaire_app.Emprunt.models import EmpruntLivre, EmpruntDvd, EmpruntCd
from datetime import date


def listeemprunt(request):
    """
    Méthode permettant de d'afficher la liste des emprunts.
    """
    emprunt_livres = EmpruntLivre.objects.all()
    emprunt_cds = EmpruntCd.objects.all()
    emprunt_dvds = EmpruntDvd.objects.all()
    return render(request, 'Emprunt/Emprunt/listEmprunt.html',
                  {'emprunt_livres': emprunt_livres, 'emprunt_cds': emprunt_cds, 'emprunt_dvds': emprunt_dvds})


def empruntmedia(model, model2, related_models, request, _id):
    """
    Méthode de base pour les emprunts.
    """
    if request.method == 'POST':
        media = model.objects.get(pk=_id)
        creationemprunt = CreationEmprunt(request.POST)
        if creationemprunt.is_valid():
            value = creationemprunt.cleaned_data['membre']
            membre = Emprunteur.objects.get(name=value)
            if media.disponible and membre.NbEmprunt <= 2 and not membre.bloque:
                membre.NbEmprunt += 1
                membre.save()
                media.disponible = False
                media.save()
                if related_models == 'livre':
                    membre.livres.add(media)
                elif related_models == 'cd':
                    membre.cds.add(media)
                elif related_models == 'dvds':
                    membre.dvds.add(media)
            else:
                membre.bloque = True
                membre.save()
                return render(request, 'Emprunt/Erreur/Error_livre.html')
            emprunteurs = model2.objects.all()
            return render(request, 'Emprunt/Emprunt/listEmprunt.html',
                          {'emprunteurs': emprunteurs})
    else:
        creationemprunt = CreationEmprunt()
        return render(request,
                      'Emprunt/Emprunt/Empruntlivre.html',
                      {'creationemprunt': creationemprunt}
                      )


def empruntlivre(request, _id):
    """
        Méthode permettant de d'ajouter un emprunt et ainsi de lier un membre à un livre en base de données.
        """
    emprunt = empruntmedia(Livre, EmpruntLivre, 'livre', request, _id)
    return emprunt


def empruntdvd(request, _id):
    """
    Méthode permettant de d'ajouter un emprunt et ainsi de lier un membre à un dvd en base de données.
    """
    emprunt = empruntmedia(Dvd, EmpruntDvd, 'dvd', request, _id)
    return emprunt


def empruntcd(request, _id):
    """
    Méthode permettant de d'ajouter un emprunt et ainsi de lier un membre à un cd en base de données.
    """
    emprunt = empruntmedia(Cd, EmpruntCd, 'cd', request, _id)
    return emprunt


def retourmedia(model, model2, related_models, request, _id):
    """ Méthode permettant défaire une jointure existante entre un emprunteur et un livre."""
    if request.method == 'POST':
        emprunt = model2.objects.get(pk=_id)
        retouremprunt = RetourEmprunt(request.POST)
        if retouremprunt.is_valid():
            value1 = retouremprunt.cleaned_data['membre']
            membre = Emprunteur.objects.get(name=value1)
            value2 = retouremprunt.cleaned_data['media']
            media = model.objects.get(name=value2)
            if not media.disponible:
                membre.NbEmprunt -= 1
                if membre.bloque:
                    membre.bloque = False
                membre.save()
                media.disponible = True
                media.save()
                if date.today() > emprunt.dateEmprunt_max:
                    membre.bloque = True
                    membre.save()
                if related_models == 'livre':
                    membre.livres.remove(media)
                elif related_models == 'cd':
                    membre.cds.remove(media)
                elif related_models == 'dvds':
                    membre.dvds.remove(media)
            emprunteurs = model2.objects.all()
            return render(request, 'Emprunt/Emprunt/listEmprunt.html',
                          {'emprunteurs': emprunteurs})
    else:
        retouremprunt = RetourEmprunt()
        return render(request,
                      'Emprunt/Retour/retourlivre.html',
                      {'retouremprunt': retouremprunt}
                      )


def retourlivre(request, _id):
    """ Méthode permettant défaire une jointure existante entre un emprunteur et un livre."""
    retour = retourmedia(Livre, EmpruntLivre, 'livre', request, _id)
    return retour


def retourdvd(request, _id):
    """ Méthode permettant défaire une jointure existante entre un emprunteur et un dvd."""
    retour = retourmedia(Dvd, EmpruntDvd, 'dvd', request, _id)
    return retour


def retourcd(request, _id):
    """ Méthode permettant défaire une jointure existante entre un emprunteur et un cd."""
    retour = retourmedia(Cd, EmpruntCd, 'cd', request, _id)
    return retour
