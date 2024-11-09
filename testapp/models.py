from django.db import models
from django.contrib.auth.models import AbstractUser
# from testdjango.manage import main
# Create your models here.
# Models cours
class Ecole(models.Model):
    
    ecoles=models.CharField(max_length=50,null=True)
    def __str__(self):
        return self.ecoles
class Classes(models.Model):
    
    classe=models.CharField(max_length=50, default="")
    def __str__(self):
        return self.classe
class Matieres(models.Model):
     
     matieres=models.CharField(max_length=50)
     def __str__(self):
        return self.matieres
class Devoir(models.Model):
     statuts={
         'traiter':'traiter',
         'enoncer':'enoncer'
         
     }
     classe=models.ForeignKey(Classes,on_delete=models.CASCADE)
     ecole=models.ForeignKey(Ecole,on_delete=models.CASCADE)
     matieres=models.ForeignKey(Matieres, on_delete=models.CASCADE)
     date_ajout=models.DateField(auto_now=True, auto_now_add=False)
     fichier =models.FileField(upload_to='devoir', max_length=100,null=True,blank=True)
     num_devoir= models.CharField(max_length=50,null=False,blank=True)
     statut = models.CharField(max_length=50,choices=statuts,blank=True, null=True)
     image_sujet=models.ImageField(upload_to="devoir",null=True,blank=True)
class Traiter(models.Model):
     statuts={
         'traiter':'traiter',
         'enoncer':'enoncer',
         'noter':'noter'
         
     }
     classe=models.ForeignKey(Classes,on_delete=models.CASCADE)
     ecole=models.ForeignKey(Ecole,on_delete=models.CASCADE)
     matieres=models.ForeignKey(Matieres, on_delete=models.CASCADE)
     traiter=models.ImageField(upload_to="devoir",null=True,blank=True)
     num_devoir= models.CharField(max_length=50,null=False,blank=True)
     note= models.FloatField(null=True,blank=True)
     statut = models.CharField(max_length=50,choices=statuts,blank=True, null=True)
     date_ajout=models.DateField(auto_now=True, auto_now_add=False)
     email=models.EmailField(max_length=50,null=False,blank=True)
class Cours(models.Model):
    
    classe=models.ForeignKey(Classes,on_delete=models.CASCADE)
    ecole=models.ForeignKey(Ecole,on_delete=models.CASCADE,null=False,default="")
    prof=models.CharField(max_length=50,null=False)
    matieres=models.ForeignKey(Matieres, on_delete=models.CASCADE)
    titre=models.CharField(max_length=50)
    date_ajout=models.DateField(auto_now=True, auto_now_add=False)
    cours =models.FileField(upload_to='pdf', max_length=100,null=True)
    phone = models.IntegerField(unique=False,null=True)
    

# MODELS INSCRIPTIONS

class UserForm(AbstractUser):
    
   
    classe=models.ForeignKey(Classes,on_delete=models.CASCADE,null=True,blank=True)
    ecole=models.ForeignKey(Ecole,on_delete=models.CASCADE,null=True,blank=True)
    matieres=models.ForeignKey(Matieres, on_delete=models.CASCADE,null=True,blank=True)
    email = models.EmailField(max_length=50,unique=True)
    phone = models.IntegerField(unique=True,null=True)
    date_aj=models.DateField(auto_now=True, auto_now_add=False)
    username=models.CharField(unique=False,blank=True,null=True,max_length=50)

    USERNAME_FIELD='email'
    REQUIRED_FIELDS=['username']

    def __str__(self):
        return self.email
    
