from django.db.models import *
from django.shortcuts import render
from apps.home.views.fcts import *
from apps.home.decorators import *
from .functions import *



def equipe_dash(request,equ_id):
    context = {}
    context["equipe"] = Equipe.objects.get(id=equ_id)
    context["nbr_chers"] = equipe_chers(equ_id).count()
    context["nbr_citations"] = equipe_chers(equ_id).aggregate(Sum("citations"))["citations__sum"]
    context["nbr_articles"] = equipe_chers(equ_id).aggregate(Sum("nbr_pubs"))["nbr_pubs__sum"]
    context["citations_per_year"] = citations_researchers_8years(equipe_chers(equ_id))
    context["citation_chers"] = citations_chers(equipe_chers(equ_id))
    # context = Dash_Equipe_calc(get_equipe_id(request))
    # equipe = Equipe.objects.get(chef_equipe=request.user.id).id
    # context["rs_citations"] = list(equipe_chers(equipe))
    # context["equipe_articles"] = equipe_articles(equipe.id)
    return render (request,'home/equipe/dashboard.html',context) 


def citations_chers(chers):
    graph = []
    if chers.count() < 10 :
        for cher in chers:
            graph.append({"cher" : cher , "citations": cher.citations})
    else:
        for cher in chers[:10]:
            graph.append({"cher" : cher , "citations": cher.citations})
    return graph

        


def equipe_chers_dash(request,equ_id):
    # inter=get_equipe_id(request)
    # liste = CherList_equipe (inter)
    # info_equipe = Equipe.objects.get(pk = inter)
    # context ={'liste':liste}
    # context["info_equipe"] = info_equipe
    context={}
    # top 5 researchers in the team with citations percentage 
    # 
    # return render (request,'home/equipe/liste_chercheur.html',context)
    return render (request,'home/equipe/equipe-chers-liste.html',context)

def equipe_chers_liste(request):
    # chercheurs citaion percentage of a team 
    # nbr citation of a researcher 
    # nbr article of a researcher 
    # plus cited article 
    context ={}
    return render (request,'home/equipe/equipe-chers-liste.html',context)

def Dash_Equipe(request,pk):
    context = Dash_Equipe_calc(pk)
    return render (request,'home/equipe/dashboard.html',context)
