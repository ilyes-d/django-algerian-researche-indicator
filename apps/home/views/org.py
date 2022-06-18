from multiprocessing import context
from django.shortcuts import render
from requests import request
from apps.home.models import *
from apps.home.views.functions import *
from ..decorators import *
from django.views.generic.list import ListView
from django.contrib.auth.decorators import *
from django.db.models import *
from .queries import *
from .filters import * 

def refrech_database(request):
    researchers_list = Researcher.objects.filter(Q(google_scholar_account__isnull=False))
    if researchers_list:
        for researcher in researchers_list:
            print(researcher)
            load_reseacher_gs_data(researcher)
        return redirect('org-carte')
    return render(request , 'refrech.html')
    

@login_required
def org_carte(request):
    context = {}
    context["nbr_etablisements"] = Etablisment.objects.filter().count()
    context["nbr_divisions"] = Division.objects.filter().count()
    context["nbr_equipes"] = Equipe.objects.filter().count()
    context["nbr_researchers"] = Researcher.objects.filter().count()
    context["total_articles"] = Researcher.objects.all().aggregate(Sum("nbr_pubs"))["nbr_pubs__sum"]
    context["wilaya_etas"] = wilaya_dash()
    context["total_citations_graph"]= final_8years_citations_all_etas()
    total_citations = []
    for citation_year in final_8years_citations_all_etas()["citations"]:
        citations_array = [str(citation_year["year"]),citation_year["citations"]]
        total_citations.append(citations_array)
    context["total_citations"] = total_citations
    
    return render(request , "home/org/org-carte.html" , context)

@login_required
def org_dashboard(request):
    context = {}
    context["nbr_etablisements"] = Etablisment.objects.filter().count()
    context["nbr_divisions"] = Division.objects.filter().count()
    context["nbr_equipes"] = Equipe.objects.filter().count()
    context["nbr_researchers"] = Researcher.objects.filter().count()
    context["total_citations"] = final_8years_citations_all_etas()
    context["all_etas_citations"] = all_etas_citations()
    return render(request , "home/org/org-dashboard.html" , context)

    
@login_required
def org_etas_dash(request):
    context = {
        'top-10-etas-citations':[],
        'top-10-etas-hindex':[],
        'nbr-etas-wilaya':0,
        'nbr':0,
    }
    return render(request, 'home/org/org-etas-dash.html', context)

@login_required
def org_etas_liste(request):
    context = {}
    context['wilayas'] = all_wilayas()
    qs = all_etas()
    context["etablisements"] = query_etablisements(qs)    
    return render(request, 'home/org/org-etas-liste.html' , context)

def wilaya_etas_liste(request):
    context = {}
    wilaya_id = request.GET.get('wilaya_id')
    if wilaya_id == '0' :
        qs = all_etas()
        etas = query_etablisements(qs)    
    else:
        qs = Etablisment.objects.filter(location=wilaya_id)
        etas = query_etablisements(qs)
    print(etas)
    context['etas'] = etas
    return render(request,'home/eta-liste.html',context)

@login_required
def org_divs_dash(request):
    context = {}
    return render(request , 'home/org/org-divs-dash.html')

def org_divs_liste(request):
    context = {}
    
    qs = Division.objects.all()
    context["wilayas"] =all_wilayas()
    context["etas"] = all_etas()
    context["divisions"] = query_divs(qs)
    return render(request, 'home/org/org-divs-liste.html',context)

def org_divs_liste_v2(request):
    context = {}
    id_wilaya = request.GET.get('id_wilaya')
    id_etablisment = request.GET.get('id_eta')
    if id_wilaya=='0':
        if id_etablisment=='0':
            qs = Division.objects.all()
        else:    
            qs = Division.objects.filter(etablisment=id_etablisment)
        context["divisions"] = query_divs(qs)
    if id_wilaya!='0':
        if id_etablisment =='0':
            qs = Division.objects.filter(etablisment__location=id_wilaya)
        else:
            qs = Division.objects.filter(Q(etablisment=id_etablisment) & Q(etablisment__location=id_wilaya))
        context["divisions"] = query_divs(qs)
    return render(request,'home/div-liste.html',context)


def org_equipes_liste(request):
    context = {}
    qs = Equipe.objects.all()
    context["wilayas"] = all_wilayas()
    context["etas"] = all_etas()
    context["divs"] = all_divs()
    context["equipes"] = query_equipes(qs)
    return render(request , 'home/org/org-equipes-liste.html',context)


def org_members_liste(request):
    context = {}
    qs = Researcher.objects.filter(equipe_researchers__isnull=False)
    context['wilayas']=all_wilayas()
    context['etas'] = all_etas()
    context['divs'] = all_divs()
    context['equipes']=all_equipes()
    context["researchers"] = qs
    return render(request , 'home/org/org-members-liste.html', context)


def members_liste_filter(id_wilaya,id_eta,id_div,id_equipe):
    qs = Researcher.objects.filter(equipe_researchers__isnull=False)
    if id_wilaya != '0':
        qs = qs.filter(equipe_researchers__division__etablisment__location=id_wilaya)
    if id_eta != '0':
        qs = qs.filter(equipe_researchers__division__etablisment=id_eta)
    if id_div != '0':
        qs = qs.filter(equipe_researcher__equipe__division=id_div)
    if id_equipe!='0':
        qs = qs.filter(equipe_researcher=id_equipe)            
    return qs
        
def members_liste(request):
    context = {}
    id_wilaya = request.GET.get('id_wilaya')
    id_eta = request.GET.get('id_eta')
    id_div = request.GET.get('id_div')
    id_equipe = request.GET.get('id_equipe')
    context['researchers'] = members_liste_filter(id_wilaya,id_eta,id_div,id_equipe)
    return render(request , 'home/members-liste.html', context)
    
            

        
def org_chef_eta_liste(request):
    context = {}
    return render(request ,'home/chers/chef-eta.html',context)
def org_chef_div_liste(request):
    context = {}
    return render(request ,'home/chers/chef-div.html',context)

def org_chef_equ_liste(request):
    context = {}
    return render(request ,'home/chers/chef-equ.html',context)

def load_etas(request):
    context={}
    id_wilaya = request.GET.get('id_wilaya')
    qs =  all_etas()
    if id_wilaya!='0':
        qs =  Etablisment.objects.filter(location=id_wilaya)
    
    context["etas"]=  qs
    return render(request, 'home/eta-options.html', context)


def load_divs(request):
    context = {}
    id_eta = request.GET.get('id_eta')
    id_wilaya = request.GET.get('id_wilaya')
    print("fel dfas")
    qs = all_divs()
    print(qs)
    if id_wilaya != '0':
        print("hahad")
        qs = qs.filter(etablisment__location=id_wilaya)
        print(qs)
    if id_eta != '0':
        print("this is")
        qs = qs.filter(etablisment=id_eta)
    print(qs)
    context['divs'] = qs
    return render(request,'home/divs-options.html',context)