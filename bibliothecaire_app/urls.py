from bibliothecaire_app.Emprunt.urls import urlpatterns3
from bibliothecaire_app.Media.urls import urlpatterns2
from bibliothecaire_app.Membre.urls import urlpatterns1


urlpatterns = urlpatterns1
urlpatterns += urlpatterns2
urlpatterns += urlpatterns3
