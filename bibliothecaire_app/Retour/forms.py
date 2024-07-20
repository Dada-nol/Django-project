from django import forms


class RetourEmprunt(forms.Form):
    membre = forms.CharField(required=False)
    media = forms.CharField(required=False)
