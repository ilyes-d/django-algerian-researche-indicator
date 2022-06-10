from django.contrib.auth import *
from django.forms import inlineformset_factory
from django.shortcuts import get_object_or_404, redirect, render
from apps.home.models import *
from apps.home.forms import *
from apps.home.decorators import *
from apps.home.views.chef_div import *
from apps.home.decorators import *
from apps.home.views.fcts import *

def eta_dash(request):
    context = Dash_Eta_calc(get_etablisement_id(request))
    return render (request,'home/eta/dashboard.html',context)  
 
def eta_divs_dash(request):
    context ={}
    return render (request,'home/eta/dashboard.html',context)  

def eta_equipes_dash(request):
    context ={}
    return render (request,'home/eta/dashboard.html',context)  

def dash_etablisemnts(request,pk):
    context = Dash_Eta_calc(pk)
    return render (request,'dashboardEta.html',context)


def Liste_division_Eta_aff_list(request):
    inter=get_etablisement_id(request)
    liste = DivsionList_Eta(inter)
    info_etablisment = Etablisment.objects.get(pk = inter)
    context ={'liste':liste}
    context["info_etablisment"] = info_etablisment
    return render (request,'home/eta/liste_div.html',context)

def eta_equipes_liste(request):
    inter=get_etablisement_id(request)
    liste = EquipeList_Eta(inter)
    info_etablisment = Etablisment.objects.get(pk = inter)
    context ={'liste':liste}
    context["info_etablisment"] = info_etablisment
    return render (request,'home/eta/liste_equipe.html',context)


def eta_chers_dash(request):
    context = {}
    return render (request,'home/eta/eta-chers-dash.html',context)
    
def eta_chers_liste(request):
    inter=get_etablisement_id(request)
    liste = CherList_eta(inter)
    info_etablisment = Etablisment.objects.get(pk = inter)
    context ={'liste':liste}
    context["info_etablisment"] = info_etablisment
    return render (request,'home/eta/liste_chercheur.html',context)

def Liste_cher_Eta_aff_list(request):
    inter=get_etablisement_id(request)
    liste = CherList_eta(inter)
    info_etablisment = Etablisment.objects.get(pk = inter)
    context ={'liste':liste}
    context["info_etablisment"] = info_etablisment
    return render (request,'home/eta/liste_chercheur_card.html',context)


def equipes_of_etablisement(request):
    return render(request , 'home/eta/equipes_of_etablisement.html')

