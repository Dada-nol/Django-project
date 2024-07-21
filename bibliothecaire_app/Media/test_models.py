""" Test pour la création et la récupération d'une donnée."""

import pytest
from bibliothecaire_app.Media.models import Livre, Cd, Dvd


@pytest.fixture
def my_media():
    """ Création d' instances de Livre, Cd et Dvd pour les tests"""
    Livre.objects.create(name='Harry Potter', auteur='J.K.Rowling')
    Livre.objects.create(name='Harry Potter 2', auteur='J.K.Rowling')
    Cd.objects.create(name="L'heure miroir", artiste='Thibault Cauvin')
    Dvd.objects.create(name='Le Seigneur des Anneaux', realisateur='Elijah Wood')


@pytest.mark.django_db
def test_my_media(my_media):
    """ Récupère l'emprunteur créé """
    livre = Livre.objects.get(name='Harry Potter')
    # Compare le nom de l'emprunteur
    assert livre.name == 'Harry Potter'
    assert livre.disponible == True


@pytest.mark.django_db
def test_list_all_media(my_media):
    """Récupère tous les emprunteurs de la base de données"""
    livres = Livre.objects.all()
    cds = Cd.objects.all()
    dvds = Dvd.objects.all()

    assert len(livres) == 2
    assert len(cds) == 1
    assert len(dvds) == 1

    names = [livre.name for livre in livres]
    names += [cd.name for cd in cds]
    names += [dvd.name for dvd in dvds]
    assert 'Harry Potter' in names
    assert "L'heure miroir" in names
    assert 'Le Seigneur des Anneaux' in names
