"""Url's for bibliothecaire_app project"""

from bibliothecaire_app.Emprunt.urls import urlpatterns3
from bibliothecaire_app.Media.urls import urlpatterns2
from bibliothecaire_app.Membre.urls import urlpatterns1
from member_app.member.urls import urlpatterns4


urlpatterns = urlpatterns1
urlpatterns += urlpatterns2
urlpatterns += urlpatterns3
urlpatterns += urlpatterns4
