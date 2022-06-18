from django.shortcuts import render
from requests import request
from apps.home.models import *
from apps.home.views.functions import *
from ..decorators import *
from django.views.generic.list import ListView
from django.contrib.auth.decorators import *
from django.db.models import *


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
    context["etablisements"] = query_all_etablisements()
    return render(request, 'home/org/org-etas-liste.html' , context)


@login_required
def org_divs_dash(request):
    context = {}
    return render(request , 'home/org/org-divs-dash.html')

def org_divs_liste(request):
    context = {}
    context["divisions"] = query_all_divs()
    return render(request, 'home/org/org-divs-liste.html',context)

def org_equipes_dash(request):
    context = {}
    return render(request , 'home/org/org-equipes-dash.html',context)

def org_equipes_liste(request):
    context = {}
    context["equipes"] = query_all_equipes()
    return render(request , 'home/org/org-equipes-liste.html',context)

def org_chers_dash(request):
    context = {}
    return render(request , 'home/org/org-chers-dash.html',context)
def org_members_liste(request):
    context = {}
    # context["researchers"] = query_all_researchers()
    return render(request , 'home/org/org-chers-liste.html', context)

def org_chef_eta_liste(request):
    context = {}
    return render(request ,'home/chers/chef-eta.html',context)
def org_chef_div_liste(request):
    context = {}
    return render(request ,'home/chers/chef-div.html',context)

def org_chef_equ_liste(request):
    context = {}
    return render(request ,'home/chers/chef-equ.html',context)

# Try 
class EtablisementListView(ListView):
    model= Etablisment
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        return context
