""" Test pour la vérifier si la relation entre les models fonctionne."""

import pytest
from bibliothecaire_app.Media.models import Livre
from bibliothecaire_app.Membre.models import Emprunteur
from bibliothecaire_app.Emprunt.models import EmpruntLivre


@pytest.fixture
def my_relations():
    """ Crée des emprunteurs et des livres """
    emprunteur1 = Emprunteur.objects.create(name='Jhon Doe')
    emprunteur2 = Emprunteur.objects.create(name='Will Smith')

    livre1 = Livre.objects.create(name='Harry Potter', auteur='J.K.Rowling')
    livre2 = Livre.objects.create(name='Harry Potter 2', auteur='J.K.Rowling')
    livre3 = Livre.objects.create(name='Le Petit Prince', auteur='Antoine de Saint-Exupéry')
    livre4 = Livre.objects.create(name='Harry Potter 3', auteur='J.K.Rowling')

    EmpruntLivre.objects.create(membre=emprunteur1, livre=livre1)
    EmpruntLivre.objects.create(membre=emprunteur1, livre=livre2)
    EmpruntLivre.objects.create(membre=emprunteur2, livre=livre3)
    EmpruntLivre.objects.create(membre=emprunteur2, livre=livre4)

    return emprunteur1, emprunteur2, livre1, livre2, livre3, livre4


@pytest.mark.django_db
def test_my_relations(my_relations):
    emprunteur1, emprunteur2, livre1, livre2, livre3, livre4 = my_relations

    emprunteur1_livres = emprunteur1.livres.all()
    assert livre1 in emprunteur1_livres
    assert livre2 in emprunteur1_livres

    emprunteur2_livres = emprunteur2.livres.all()
    assert livre3 in emprunteur2_livres
    assert livre4 in emprunteur2_livres
    assert livre2 not in emprunteur2_livres

    emprunt_livre = EmpruntLivre.objects.filter(membre=emprunteur1, livre=livre1).first()
    assert emprunt_livre is not None
    assert emprunt_livre.dateEmprunt is not None
