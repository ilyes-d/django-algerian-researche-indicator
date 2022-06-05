from django.shortcuts import render
from apps.home.views.fcts import *
from apps.home.decorators import *
from .functions import *

def equipe_dash(request):
    context = Dash_Equipe_calc(get_equipe_id(request))
    equipe = Equipe.objects.get(chef_equipe=request.user.id)
    context["equipe_articles"] = equipe_articles(equipe.id)
    return render (request,'home/equipe/dashboard.html',context) 


def equipe_chers_dash(request):
    inter=get_equipe_id(request)
    liste = CherList_equipe (inter)
    info_equipe = Equipe.objects.get(pk = inter)
    context ={'liste':liste}
    context["info_equipe"] = info_equipe
    return render (request,'home/equipe/liste_chercheur.html',context)

def equipe_chers_liste(request):
    context ={}
    return render (request,'home/equipe/equipe-chers-liste.html',context)

def Dash_Equipe(request,pk):
    context = Dash_Equipe_calc(pk)
    return render (request,'home/equipe/dashboard.html',context)
