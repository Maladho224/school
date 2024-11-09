from django import forms
from django.contrib.auth.forms import UserCreationForm
import django.db
from .models import *

class up_form(UserCreationForm):
    class Meta:
        model=UserForm
        fields=('email','password1','password2','phone','username','ecole')
class LoginForm(forms.Form):
    email =forms.CharField(max_length=100,label='email')
    password=forms.CharField(max_length=40, required=True,label="Mot de passe")
   
class Add_coursForm(forms.ModelForm):
    class Meta:
        model = Cours
        fields='__all__'
class UpdateCours(forms.ModelForm):
    class Meta:

        model = Cours
        fields = '__all__'
class UpdateEffectif(forms.ModelForm):
    class Meta:

        model = UserForm
        # fields='__all__'
        fields = ('classe','ecole','matieres','username','email','phone','groups')
        
class UpdateDevoir(forms.ModelForm):
    class Meta:
        model = Devoir
        fields = '__all__'
class DevoirForm(forms.ModelForm):
    class Meta:
        model = Devoir
        fields='__all__'
class FormTraiter(forms.ModelForm):
    class Meta:
        model = Traiter
        fields = ('traiter','num_devoir','classe','matieres','ecole','statut','email')
class UpdateTraiter(forms.ModelForm):
    class Meta:
        model = Traiter
        fields = '__all__'