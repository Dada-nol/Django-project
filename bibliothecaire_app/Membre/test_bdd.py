class DD():
    name = "se"
    NbEmprunt = 0
    bloque = 0


def test_liste_membre():
    membre = DD
    assert membre.name == "Dada"
    membre.NbEmprunt = 0
    membre.bloque = 0
