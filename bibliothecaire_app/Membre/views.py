""" Ce fichier contient l'ensemble des fonctions pour afficher, créer, modifieret supprimer un membre. """

from django.shortcuts import render
from bibliothecaire_app.Membre.forms import CreationMembre, UpdateMembre
from bibliothecaire_app.Membre.models import Emprunteur


def liste_membre(request):
    """
    Méthode permettant de d'afficher la liste des membres.
    """
    membres = Emprunteur.objects.all()
    return render(request, 'Membres/list.html',
                  {'membres': membres})


def ajout_membre(request):
    """
    Méthode permettant de d'ajouter un membre en base de données.
    """
    if request.method == 'POST':
        creationmembre = CreationMembre(request.POST)
        if creationmembre.is_valid():
            membre = Emprunteur()
            membre.name = creationmembre.cleaned_data['name']
            membre.save()
            membres = Emprunteur.objects.all()
            return render(request, 'Membres/list.html',
                          {'membres': membres})
    else:
        creationmembre = CreationMembre()
        return render(request,
                      'Membres/ajoutMembre.html',
                      {'creationmembre': creationmembre}
                      )


def update_membre(request, _id):
    """
    Méthode permettant de de modifier membre déjà existant.
    """
    if request.method == 'POST':
        membre = Emprunteur.objects.get(pk=_id)
        updatemembre = UpdateMembre(request.POST)
        if updatemembre.is_valid():
            membre.name = updatemembre.cleaned_data['name']
            membre.save()
        membres = Emprunteur.objects.all()
        return render(request, 'Membres/list.html',
                      {'membres': membres})
    else:
        updatemembre = UpdateMembre()
        return render(request,
                      'Membres/updateMembre.html',
                      {'updatemembre': updatemembre}
                      )


def delete_membre(request, _id):
    """
    Méthode permettant de de supprimer un membre.
    """
    membre = Emprunteur.objects.get(pk=_id)
    membre.delete()
    membres = Emprunteur.objects.all()
    return render(request, 'Membres/list.html',
                  {'membres': membres})
