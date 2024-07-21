""" Test pour la création et la récupération d'une donnée."""

import pytest
from bibliothecaire_app.Membre.models import Emprunteur


@pytest.fixture
def my_emprunteur():
    """ Création d'une instance de Emprunteur pour les tests"""
    Emprunteur.objects.create(name='value1')
    Emprunteur.objects.create(name='value2')
    Emprunteur.objects.create(name='value3')


@pytest.mark.django_db
def test_my_user(my_emprunteur):
    """ Récupère l'emprunteur créé """
    membre = Emprunteur.objects.get(name='value1')
    # Compare le nom de l'emprunteur
    assert membre.name == 'value1'
    assert membre.bloque == False
    assert membre.NbEmprunt == 0


@pytest.mark.django_db
def test_list_all_emprunteurs(my_emprunteur):
    """Récupère tous les emprunteurs de la base de données"""
    emprunteurs = Emprunteur.objects.all()

    assert len(emprunteurs) == 3

    names = [emprunteur.name for emprunteur in emprunteurs]
    assert 'value1' in names
    assert 'value2' in names
    assert 'value3' in names
