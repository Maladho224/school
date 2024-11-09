
from django.urls import path
from .views import *
from django.conf import settings

from django.conf.urls.static import static
urlpatterns = [
    path('',register, name="register"),
    path('connexion',connexion, name="connexion"),
    path('acceuil',acceuil, name="acceuil"),
    path('cours',cours, name="cours"),
    path('Add_cours',Add_cours,name="Add_cours"),
    path('detailsCours/<int:myid>',detailsCours,name='detailsCours'),
    path('modifierCours/<int:myid>',modifierCours,name="modifierCours"),
    path('deleteCours/<int:myid>',deleteCours,name="deleteCours"),
    
    path('deconnexion',deconnexion, name='deconnexion'),
    
    path('effectifs',effectifs,name='effectifs'),
    path('modifiereffectifs/<int:myid>',modifiereffectifs,name='modifiereffectifs'),
    path('deleteeffectifs/<int:myid>',deleteeffectifs,name='deleteeffectifs'),
    path('devoir',devoir,name='devoir'),
    path('Add_devoir',Add_devoir,name='Add_devoir'),
    
    path('modifierDevoirs/<int:myid>',modifierDevoirs,name='modifierDevoirs'),
    
    path('deleteDevoirs/<int:myid>',deleteDevoirs,name='deleteDevoirs'),
    path('traiterDevoir',traiterDevoir,name='traiterDevoir'),
    path('traiter',traiter,name='traiter'),
    path('updateTraiter/<int:id_traiter>',updateTraiter,name='updateTraiter'),
    path('deleteTraiter/<int:id_traiter>',deleteTraiter,name="deleteTraiter"),

]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
