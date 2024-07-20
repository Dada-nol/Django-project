"""Url's for bibliothecaire_app project"""

from django.urls import path
from bibliothecaire_app.Membre import views

urlpatterns1 = [
    path('', views.liste_membre),
    path('ajoutMembre/', views.ajout_membre),
    path('updateMembre/<int:_id>/', views.update_membre),
    path('deleteMembre/<int:_id>/', views.delete_membre)
]
