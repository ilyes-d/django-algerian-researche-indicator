


from pyexpat.errors import messages
from django.shortcuts import redirect, render

from apps.home.forms import *
from apps.home.models import Division, Equipe, Etablisment


def creat_Etablisment_views(request):
    form =EtablismentForm(data=request.POST)
    if request.method =="POST":     
        if form.is_valid() :
             form.save()
             return redirect("org-etas-liste")
        return render(request,"crud/creatEtablisment.html",{"form":form})

    else:
           form=EtablismentForm
           return render(request,'crud/creatEtablisment.html',{"form":form})
       
       
#supprimer etablissment
def Delete_Etablisment_views (request,pk):
    Etu=Etablisment.objects.get(id=pk)
    Etu.delete()
    return redirect('org-etas-liste')  


def creat_division_views(request):
   form = DivisionForm(data=request.POST)
   if request.method =="POST":     
        if form.is_valid() :
             form.save()
             return redirect("org-divs-liste")
        return render(request,"crud/creatDiv.html",{"form":form})

   else:
        form= DivisionForm
        return render(request,'crud/creatDiv.html',{"form":form})
       
       
def Delete_Division_views (request,pk):
    Etu=Division.objects.get(id=pk)
    Etu.delete()
    return redirect('org-divs-liste')


def creat_equipe_views(request):
   form = EquipeForm(data=request.POST)
   if request.method =="POST":     
        if form.is_valid() :
             form.save()
             return redirect("org-equipes-liste")
        return render(request,"crud/creatEquipe.html",{"form":form})

   else:
        form=  EquipeForm
        return render(request,'crud/creatEquipe.html',{"form":form})
       
       
def Delete_Equipe_views (request,pk):
    Etu=Equipe.objects.get(id=pk)
    Etu.delete()
    return redirect('org-equipes-liste')