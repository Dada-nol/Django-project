""" Formulaires permettant la création de média."""

from django import forms


class CreationMedia(forms.Form):
    name = forms.CharField(required=False)
    disponible = forms.BooleanField(required=False)
    createur = forms.CharField(required=False)
