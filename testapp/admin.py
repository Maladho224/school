from django.contrib import admin
# from testapp.views import Add_cours
from .models import *
# Register your models here.
class DisplayUser(admin.ModelAdmin):
    list_display=('email','last_name','first_name','classe','date_aj','matieres','ecole')

class DisplayCours(admin.ModelAdmin):
    list_display=('matieres','classe','prof','date_ajout','cours','ecole')

class DisplayDevoir(admin.ModelAdmin):
    list_display=('matieres','classe','date_ajout','fichier','image_sujet','num_devoir','ecole')
class DisplayTraiter(admin.ModelAdmin):
    list_display=('matieres','classe','date_ajout','traiter','note','num_devoir','ecole','statut')

admin.site.register(UserForm,DisplayUser)

admin.site.register(Cours,DisplayCours)
admin.site.register(Classes)
admin.site.register(Ecole)
admin.site.register(Matieres)
admin.site.register(Traiter,DisplayTraiter)
admin.site.register(Devoir,DisplayDevoir)

# admin.site.register(Role)
admin.site.site_header="SITE D'ADMINISTRATION DU SITE DE GEST-SCHOOL"
admin.site.site_title="GEST-SCHOOL"
admin.autodiscover()