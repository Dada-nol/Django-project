from django.shortcuts import render
from bibliothecaire_app.Retour.forms import RetourEmprunt
from bibliothecaire_app.Membre.models import Emprunteur
from bibliothecaire_app.Media.models import Livre
from bibliothecaire_app.Emprunt.models import EmpruntLivre
from datetime import date


def retourlivre(request, id):
    if request.method == 'POST':
        emprunt = EmpruntLivre.objects.get(pk=id)
        retouremprunt = RetourEmprunt(request.POST)
        if retouremprunt.is_valid():
            value1 = retouremprunt.cleaned_data['membre']
            membre = Emprunteur.objects.get(name=value1)
            value2 = retouremprunt.cleaned_data['media']
            livre = Livre.objects.get(name=value2)
            if not livre.disponible:
                membre.NbEmprunt -= 1
                membre.save()
                livre.disponible = True
                livre.save()
                if date.today() > emprunt.dateEmprunt_max:
                    membre.bloque = True
                    membre.save()
                membre.livres.remove(livre)
            emprunteurs = EmpruntLivre.objects.all()
            return render(request, 'Emprunt/Emprunt/listEmprunt.html',
                          {'emprunteurs': emprunteurs})
    else:
        retouremprunt = RetourEmprunt()
        return render(request,
                      'Emprunt/Retour/retourcd.html',
                      {'retouremprunt': retouremprunt}
                      )
