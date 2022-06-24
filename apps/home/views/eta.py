from multiprocessing import context
from django.db.models import *
from django.contrib.auth import *
from django.forms import inlineformset_factory
from django.shortcuts import get_object_or_404, redirect, render
from requests import request
from apps.home.models import *
from apps.home.forms import *
from apps.home.decorators import *
from apps.home.views.div import *
from apps.home.decorators import *
from apps.home.views.fcts import *
from .functions import *
from .queries import *

# nbr citations par divisions 
# 

def eta_dash(request,eta_id):
    context = {}
    context["eta"] = Etablisment.objects.get(id=eta_id)
    context["nbr_divisions"] = eta_divs(eta_id).count()
    context["nbr_equipes"] = eta_equipes(eta_id).count()
    context["nbr_chers"] = eta_chers(eta_id).count()
    context["citations"] = eta_chers(eta_id).aggregate(Sum("citations"))["citations__sum"]
    context["articles"] = eta_chers(eta_id).aggregate(Sum("nbr_pubs"))["nbr_pubs__sum"]
    context["eta_divs_citations"] = eta_divs_citations(eta_id)
    context["citations_total_8year"] = citations_researchers_8years(eta_chers(eta_id))
    context["chers5_citations"]=  top_5_researchers_citations(eta_chers(eta_id))
    context["chers5_hindex"] = top_5_researchers_hindex(eta_chers(eta_id))
    context["chers5_i10index"] = top_5_researchers_i10_index(eta_chers(eta_id))
    # context["graph_"]
    # context = Dash_Eta_calc(get_etablisement_id(request))
    return render (request,'home/eta/eta-dash.html',context)



def eta_divs_citations(eta_id):
    context = []
    for div in eta_divs(eta_id):
        div_citations = div_chers(div.id).aggregate(Sum("citations"))["citations__sum"]
        context.append({"div" : div , "div_citations":div_citations})
    return context

def eta_divs_liste(request, eta_id):
    context = {}
    qs = Division.objects.filter(etablisment=eta_id)
    context["divisions"] =query_divs(qs)
    return render(request,'home/eta/eta-divs-liste.html',context)
    

# def eta_dash(request,pk):
#     context = Dash_Eta_calc(get_etablisement_id(request))
#     return render (request,'home/eta/eta-dash.html',context)  
 
def eta_divs_dash(request):
    context ={}
    return render (request,'home/eta/eta-dash.html',context)  

def eta_equipes_dash(request):
    context ={}
    return render (request,'home/eta/eta-dash.html',context)  

def dash_etablisemnts(request,pk):
    context = Dash_Eta_calc(pk)
    return render (request,'home/eta/eta-dash-pk.html',context)


def Liste_division_Eta_aff_list(request):
    inter=get_etablisement_id(request)
    liste = DivsionList_Eta(inter)
    info_etablisment = Etablisment.objects.get(pk = inter)
    context ={'liste':liste}
    context["info_etablisment"] = info_etablisment
    return render (request,'home/eta/liste_div.html',context)

def eta_equipes_liste(request,eta_id):
    context = {}
    # inter=get_etablisement_id(request)
    # liste = EquipeList_Eta(inter)
    # info_etablisment = Etablisment.objects.get(pk = inter)
    # context ={'liste':liste}
    # context["info_etablisment"] = info_etablisment
    qs = Equipe.objects.filter(division__etablisment=eta_id)
    context["equipes"] = query_equipes(qs)
    return render (request,'home/eta/liste_equipe.html',context)

def eta_members_liste(request,eta_id):
    context = {}
    qs = Researcher.objects.filter(equipe_researchers__division__etablisment=eta_id)
    context["researchers"] = qs
    return render(request , 'home/eta/eta-members-liste.html',context)


def eta_chefdiv(request,eta_id):
    context = {}
    qs = Researcher.objects.filter(division__etablisment=eta_id)
    context['researchers'] = qs
    return render(request , 'home/eta/eta-chefdiv-liste.html',context)
    

def eta_chefequ(request,eta_id):
    context = {}
    qs = Researcher.objects.filter(equipe__division__etablisment=eta_id)
    context['researchers'] = qs
    return render(request , 'home/eta/eta-chefequ-liste.html',context)




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

