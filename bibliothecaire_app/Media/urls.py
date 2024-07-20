"""Url's for bibliothecaire_app project"""

from django.urls import path
from bibliothecaire_app.Media import views

urlpatterns2 = [
    path('listMedia/', views.listemedia),
    path('ajout-livre/', views.ajoutlivre),
    path('ajout-dvd/', views.ajoutdvd),
    path('ajout-cd/', views.ajoutcd),
    path('ajout-jdp/', views.ajoutjdp)
]
