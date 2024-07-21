"""Url's for bibliothecaire_app project"""

from django.urls import path
from bibliothecaire_app.Emprunt import views

urlpatterns3 = [
    path('listEmprunt/', views.listeemprunt),
    path('Empruntlivre/<int:_id>/', views.empruntlivre),
    path('Empruntdvd/<int:_id>/', views.empruntdvd),
    path('Empruntcd/<int:_id>/', views.empruntcd),
    path('error_cd/', views.empruntcd),
    path('error_dvd/', views.empruntdvd),
    path('error_livre/', views.empruntlivre),
    path('retourlivre/<int:_id>/', views.retourlivre),
    path('retourdvd/<int:_id>/', views.retourdvd),
    path('retourcd/<int:_id>/', views.retourcd)
]
