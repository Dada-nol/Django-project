""" Formulaires permettant la création et la modification des membres."""

from django import forms


class CreationMembre(forms.Form):
    name = forms.CharField(required=False)


class UpdateMembre(forms.Form):
    name = forms.CharField(required=False)


