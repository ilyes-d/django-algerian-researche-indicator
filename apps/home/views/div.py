from django.db.models import *
from apps.home.decorators import *
from apps.home.views.fcts import *
from django.shortcuts import get_object_or_404, redirect, render

from apps.home.views.queries import *
from .functions import *
from .filters import *

def div_dash(request,div_id):
    context={}
    context["division"] = Division.objects.get(id=div_id)
    context["nbr_equipes"] = div_equipes(div_id).count()
    context["nbr_chers"] = div_chers(div_id).count()
    context["citations"] = div_chers(div_id).aggregate(Sum("citations"))["citations__sum"]
    context["articles"] = div_chers(div_id).aggregate(Sum("nbr_pubs"))["nbr_pubs__sum"]
    context["chers5_citations"] = top_5_researchers_citations(div_chers(div_id))
    context["citations_total_8year"] = citations_researchers_8years(div_chers(div_id))
    context["div_equipes_citations"] = div_equipes_citations(div_id)
    # context = Dash_Division_calc(get_division_id(request))
    return render (request,'home/div/div-dash.html',context) 

def div_equipes_citations(div_id):
    context = []
    for equipe in div_equipes(div_id):
        equipe_citations = equipe_chers(equipe.id).aggregate(Sum("citations"))["citations__sum"]
        context.append({"equipe" : equipe.nom , "citations": equipe_citations })
    return context
        


def dash_divisions(request,pk):
    context = Dash_Division_calc(pk)
    return render (request,'DashDivision.html',context)


def dash_divisions(request,pk):
    context = Dash_Equipe_calc(pk)
    return render (request,'DashDivision.html',context)

def DivsionList_Eta(pk):
    i = Division.objects.filter(etablisment = pk)
    return i

def div_equipe_liste(request):
    inter=get_division_id(request)
    liste = EquipeList_Div(inter)
    info_division= Division.objects.get(pk = inter)
    context ={'liste':liste}
    context["info_division"] = info_division
    return render (request,'home/division/liste_equipe.html',context)


def div_chers_liste(request):
    inter=get_division_id(request)
    liste = CherList_div (inter)
    info_division = Division.objects.get(pk = inter)
    context ={'liste':liste}
    context["info_division"] = info_division
    return render (request,'home/division/liste_chercheur.html',context)

# card profiles
def div_chers_liste_card(request):
    inter=get_division_id(request)
    liste = CherList_div (inter)
    info_division = Division.objects.get(pk = inter)
    context ={'liste':liste}
    context["info_division"] = info_division
    return render (request,'home/division/liste_chercheur_card.html',context)

def div_chers_dash(request):
    context = {}
    return render(request,'home/',context)

def div_equipe_dashboard(request):
    context = {}
    return render(request,'home/',context)
    

