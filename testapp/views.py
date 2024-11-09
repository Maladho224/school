# from urllib import request

from django.contrib import messages
from django.shortcuts import get_object_or_404, render,redirect,HttpResponse
from django.contrib.auth import login as auth_login,authenticate,logout
from django.contrib.auth.decorators import login_required,permission_required
from django.db.models import Count
from Direction.urls import *

from .forms import *
from .models import *

# Inscription
def register(request):
   
    if request.method=="POST":
        form=up_form(request.POST)
        if form.is_valid():
            
            form.save()
           
            return redirect(connexion)
    else:
        form=up_form()
    context ={
        'form':form,
    }
    return render(request,'pages/register.html',context)

def connexion(request):
        group1= request.user.groups.filter(name='ELEVES')
        group2=request.user.groups.filter(name='DIRECTION')
        group3=request.user.groups.filter(name='PROFESSEURS')
        group4=request.user.groups.filter(name='GESTIONNAIRE DU SITE')

        form = LoginForm()
        message = ''
        if request.method=="POST":
            form=LoginForm(request.POST)
        if form.is_valid():
            user = authenticate(
               request,email=form.cleaned_data['email'],
               password=form.cleaned_data['password'],
          
                               )
            if user is not None:
                auth_login(request,user)
                return redirect('acceuil')
                 
            else:
                message=f"connexion non reusi"
               
        return render(request, 'pages/connexion.html',{'form':form,'message':message})
# Acceuil des utilisateurs
@login_required(login_url='/connexion')
def acceuil(request):
    number = request.session.get('visite',0)+1
    request.session['visite']=number
    return render(request,'pages/acceuil.html',{'number':number})
# ajout d'un cours
@login_required(login_url='/connexion')
@permission_required('testapp.add_cours',raise_exception=True)
def Add_cours(request):
    if request.method =="POST":
        form =Add_coursForm(request.POST,request.FILES)
        
       
        if form.is_valid():
            ecole_user= form.cleaned_data['ecole']
            classe_user = form.cleaned_data['classe']
            matieres_user=form.cleaned_data['matieres']
           
            if request.user.ecole == ecole_user and request.user.classe ==classe_user and request.user.matieres == matieres_user :
                form.save()
                return redirect('cours')
            elif request.user.ecole == ecole_user and request.user.classe ==None and request.user.matieres == matieres_user:
                form.save()
                return redirect('cours')
            else:
             return HttpResponse("Verifier vos informations fournis")
    else:
        form=Add_coursForm()
    return render(request,'pages/Add_cours.html',{'form':form})
# Espace cours
@login_required(login_url='/connexion')
@permission_required('testapp.view_cours',raise_exception=True)
# @permission_required('testapp.delete_cours',raise_exception=True)
def cours(request):
    group1= request.user.groups.filter(name='ELEVES')
    group2=request.user.groups.filter(name='DIRECTION')
    group3=request.user.groups.filter(name='PROFESSEURS')
    group4=request.user.groups.filter(name='GESTIONNAIRE DU SITE')
    
    if request.user.is_authenticated:
            if group1:
                s=request.user.classe
                t= Cours.objects.all().filter(classe=s,ecole=request.user.ecole)
                return render(request,'pages/cours.html',{'t':t})
            elif group2: 
                # s=request.user.classe
                t= Cours.objects.all().filter(ecole=request.user.ecole)
                return render(request,'pages/cours.html',{'t':t})
            elif group3:
                s=request.user.classe
                matieres_user=request.user.matieres
                user_ecole=request.user.ecole
                t= Cours.objects.all().filter(classe=s , matieres=matieres_user,ecole=request.user.ecole)
                return render(request,'pages/cours.html',{'t':t})
            elif group4:
               
                # user_ecole=request.user.ecole
                t= Cours.objects.all().filter(ecole=request.user.ecole)
                return render(request,'pages/cours.html',{'t':t})
            else:
                return HttpResponse("Vous n'avez pas acces de voir cette liste ")
        

    else:
        return redirect('connexion')
@login_required(login_url='/connexion')

def detailsCours(request,myid):
    req= Cours.objects.get(id=myid)
    return render(request,'pages/detailsCours.html',{'req':req})
@permission_required('testapp.change_cours',raise_exception=True)
def modifierCours(request,myid):
    req=Cours.objects.get(id=myid)
    form=UpdateCours(instance=req)
    if request.method=="POST":
        form = UpdateCours(request.POST,request.FILES,instance=req)
        if form.is_valid():
            form.save()
            messages.success(request,'Modification reusi')
            return redirect('cours')
    return render(request,'pages/modifierCours.html',{'form':form})
def deleteCours(request,myid):
    obj=Cours.objects.get(id=myid)
    
    obj.delete()
    messages.success(request,'delete success')
    return redirect('cours')
    
    
    
@login_required(login_url='/connexion')
@permission_required('testapp.delete_cours',raise_exception=True)

def effectifs(request):
   
    group2=request.user.groups.filter(name='DIRECTION')
    group3=request.user.groups.filter(name='PROFESSEURS')
    group4=request.user.groups.filter(name='GESTIONNAIRE DU SITE')
    if request.user.is_authenticated:
        if group2 or group4:
            req=request.user.ecole
            t= UserForm.objects.all().filter(ecole=req)
            return render(request,'pages/effectifs.html',{'t':t})
        elif group3:
            ecole=request.user.ecole
            classe= request.user.classe
            mat=request.user.matieres
            t= UserForm.objects.all().filter(ecole=ecole,classe=classe, matieres=None)
            return render(request,'pages/effectifs.html',{'t':t})
        

        else:
            return HttpResponse("Vous n'avez pas acces de voir cette liste")
        
def modifiereffectifs(request,myid):
    req=UserForm.objects.get(id=myid)
    form=UpdateEffectif(instance=req)
    if request.method=="POST":
            form = UpdateEffectif(request.POST,instance=req)
            if form.is_valid() :
                
                form.save()
                messages.success(request,'Modification reusi')
                return redirect('effectifs')
                   
                
    return render(request,'pages/modifiereffectifs.html',{'form':form})

def deleteeffectifs(request,myid):
    obj=UserForm.objects.get(id=myid)
    
    obj.delete()
    messages.success(request,'delete success')
    return redirect('effectifs')
    
# Devoir
def devoir(request):
    group1= request.user.groups.filter(name='ELEVES')
    if group1:
        req = Devoir.objects.all().filter(ecole=request.user.ecole,classe=request.user.classe)
        return render(request,'pages/devoir.html',{'req':req})
    elif request.user.groups.filter(name='DIRECTION'):
         req = Devoir.objects.all().filter(ecole=request.user.ecole)
         return render(request,'pages/devoir.html',{'req':req})
    elif request.user.groups.filter(name='PROFESSEURS'):
        req = Devoir.objects.all().filter(ecole=request.user.ecole,classe=request.user.classe)
        return render(request,'pages/devoir.html',{'req':req})
    elif request.user.groups.filter(name='GESTIONNAIRE DU SITE'):
        req = Devoir.objects.all().filter(ecole=request.user.ecole)
        return render(request,'pages/devoir.html',{'req':req}) 
    else:
        return HttpResponse("Vous n'avez pas d'accerder ")

def Add_devoir(request):
    if request.method == "POST":
        form = DevoirForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('devoir')
    else:
        form = DevoirForm()
    return render(request,'pages/Add_devoirs.html',{'form':form})
def modifierDevoirs(request,myid):
    req=Devoir.objects.get(id=myid)
    form=UpdateDevoir(instance=req)
    if request.method=="POST":
            form = UpdateDevoir(request.POST,request.FILES,instance=req)
            if form.is_valid() :
                
                form.save()
                messages.success(request,'Modification reusi')
                return redirect('devoir')
    else:
        
     return render(request,'pages/Add_devoirs.html',{'form':form})
    
def deleteDevoirs(request,myid):
      delet=Devoir.objects.get(id=myid)
      delet.delete()
      messages.success(request,"Suppression reusi")
      return redirect('devoir')
# traiter
def traiterDevoir(request):
    if request.method=="POST":
            form = FormTraiter(request.POST,request.FILES)
            if form.is_valid() :
                
                form.save()
                messages.success(request,'Modification reusi')
                return redirect('devoir')
    else:
        form=FormTraiter()
        return render(request,'pages/Add_traiter.html',{'form':form})
    
def traiter(request):
    group1= request.user.groups.filter(name='ELEVES')
    if group1:
        req = Traiter.objects.all().filter(ecole=request.user.ecole,classe=request.user.classe,email= request.user.email)
        
        return render(request,'pages/traiter.html',{'req':req})
    elif request.user.groups.filter(name='DIRECTION'):
         req = Traiter.objects.all().filter(ecole=request.user.ecole)
         return render(request,'pages/traiter.html',{'req':req})
    elif request.user.groups.filter(name='PROFESSEURS'):
        req = Traiter.objects.all().filter(ecole=request.user.ecole,classe=request.user.classe)
        return render(request,'pages/traiter.html',{'req':req})
    elif request.user.groups.filter(name='GESTIONNAIRE DU SITE'):
        req = Traiter.objects.all().filter(ecole=request.user.ecole)
        return render(request,'pages/traiter.html',{'req':req}) 
    else:
        return HttpResponse("Vous n'avez pas accès a cet espace ")
        
def updateTraiter(request,id_traiter):
    req= Traiter.objects.get(id=id_traiter)
    form = UpdateTraiter(instance = req)
    if request.method == "POST":
        form = UpdateTraiter(request.POST,request.FILES,instance =req)
        if form.is_valid():
            form.save()
            return redirect('traiter')
        # else:
        #     form=updateTraiter()
    return render(request,'pages/updateTrater.html',{'form':form})
def deleteTraiter(request,id_traiter):
    det = Traiter.objects.get(id=id_traiter)
    det.delete()
    return redirect('traiter')
def deconnexion(request):
    logout(request)
    return redirect(connexion)

