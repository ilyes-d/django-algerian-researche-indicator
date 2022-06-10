from django.shortcuts import render
from apps.home.models import *
from apps.home.views.functions import *
from ..decorators import *
from django.views.generic.list import ListView
from django.contrib.auth.decorators import *

@login_required
def org_carte(request):
    context = {}
    context["nbr_etablisements"] = Etablisment.objects.filter().count()
    context["nbr_divisions"] = Division.objects.filter().count()
    context["nbr_equipes"] = Equipe.objects.filter().count()
    context["nbr_researchers"] = Researcher.objects.filter().count()
    context["wilaya_etas"] = wilaya_dash()
    return render(request , "home/org/org-carte.html" , context)

@login_required
def org_dashboard(request):
    context = {}
    context["nbr_etablisements"] = Etablisment.objects.filter().count()
    context["nbr_divisions"] = Division.objects.filter().count()
    context["nbr_equipes"] = Equipe.objects.filter().count()
    context["nbr_researchers"] = Researcher.objects.filter().count()
    
    # context["top_10_etas_citations"]
    context["total_citations"] = final_8years_citations_all_etas()
    # context['top10_etablisements_citations'] = top_10_citations_etas()
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
