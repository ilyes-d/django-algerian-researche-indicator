from apps.home.decorators import *
from apps.home.views.fcts import *
from django.shortcuts import get_object_or_404, redirect, render

# @is_chef_division
def dash_division(request):
    context = Dash_Division_calc(get_division_id(request))
    return render (request,'home/division/dashboard.html',context) 

@is_superuser
@is_chef_eta
def dash_divisions(request,pk):
    context = Dash_Division_calc(pk)
    return render (request,'DashDivision.html',context)


def dash_divisions(request,pk):
    context = Dash_Equipe_calc(pk)
    return render (request,'DashDivision.html',context)

def DivsionList_Eta(pk):
    i = Division.objects.filter(etablisment = pk)
    return i

def Liste_equipe_Div_aff_list(request):
    inter=get_division_id(request)
    liste = EquipeList_Div(inter)
    info_division= Division.objects.get(pk = inter)
    context ={'liste':liste}
    context["info_division"] = info_division
    return render (request,'home/division/liste_equipe.html',context)


def Liste_cher_Div_aff_list(request):
    inter=get_division_id(request)
    liste = CherList_div (inter)
    info_division = Division.objects.get(pk = inter)
    context ={'liste':liste}
    context["info_division"] = info_division
    return render (request,'home/division/liste_chercheur.html',context)

def Liste_cher_Div_aff_card(request):
    inter=get_division_id(request)
    liste = CherList_div (inter)
    info_division = Division.objects.get(pk = inter)
    context ={'liste':liste}
    context["info_division"] = info_division
    return render (request,'home/division/liste_chercheur_card.html',context)