from django.forms import inlineformset_factory
from django.shortcuts import get_object_or_404, redirect, render
from apps.home.models import *
from apps.home.forms import *
from django.contrib import messages
from django.contrib.auth import *
from apps.home.decorators import *
from apps.home.views.fcts import *
from apps.home.decorators import *
from apps.home.views.chef_div import *

@is_chef_eta
def dash_etablisemnt(request):
    context = Dash_Eta_calc(get_etablisement_id(request))
    return render (request,'home/etablisement/dashboard.html',context)  
 

@is_superuser
def dash_etablisemnts(request,pk):
    context = Dash_Eta_calc(pk)
    return render (request,'dashboardEta.html',context)


def Liste_division_Eta_aff_list(request):
    inter=get_etablisement_id(request)
    liste = DivsionList_Eta(inter)
    info_etablisment = Etablisment.objects.get(pk = inter)
    context ={'liste':liste}
    context["info_etablisment"] = info_etablisment
    return render (request,'home/etablisement/liste_div.html',context)

def Liste_equipe_Eta_aff_list(request):
    inter=get_etablisement_id(request)
    liste = EquipeList_Eta(inter)
    info_etablisment = Etablisment.objects.get(pk = inter)
    context ={'liste':liste}
    context["info_etablisment"] = info_etablisment
    return render (request,'home/etablisement/liste_equipe.html',context)

def Liste_cher_Eta_aff(request):
    inter=get_etablisement_id(request)
    liste = CherList_eta(inter)
    info_etablisment = Etablisment.objects.get(pk = inter)
    context ={'liste':liste}
    context["info_etablisment"] = info_etablisment
    return render (request,'home/etablisement/liste_chercheur.html',context)

def Liste_cher_Eta_aff_list(request):
    inter=get_etablisement_id(request)
    liste = CherList_eta(inter)
    info_etablisment = Etablisment.objects.get(pk = inter)
    context ={'liste':liste}
    context["info_etablisment"] = info_etablisment
    return render (request,'home/etablisement/liste_chercheur_card.html',context)


def equipes_of_etablisement(request):
    return render(request , 'home/etablisement/equipes_of_etablisement.html')


  