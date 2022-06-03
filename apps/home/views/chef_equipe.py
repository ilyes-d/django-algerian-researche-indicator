from django.shortcuts import get_object_or_404, redirect, render
from apps.home.views.fcts import *
from apps.home.decorators import *


def dash_equipe(request):
    context = Dash_Equipe_calc(get_equipe_id(request))
    return render (request,'home/equipe/dashboard.html',context) 



def equipe_dashboard(request):
    pass

def Liste_cher_Equipe_aff_list(request):
    inter=get_equipe_id(request)
    liste = CherList_equipe (inter)
    info_equipe = Equipe.objects.get(pk = inter)
    context ={'liste':liste}
    context["info_equipe"] = info_equipe
    return render (request,'home/equipe/liste_chercheur.html',context)

def Dash_Equipe(request,pk):
    context = Dash_Equipe_calc(pk)
    return render (request,'home/equipe/dashboard.html',context)