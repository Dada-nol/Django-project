""" Formulaires permettant la création d'un emprunt."""

from django import forms


class CreationEmprunt(forms.Form):
    membre = forms.CharField(required=False)


