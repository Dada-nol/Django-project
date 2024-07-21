"""Url's for member_app project"""

from django.urls import path
from member_app.member import views

urlpatterns4 = [
    path('', views.listemedia)
]
