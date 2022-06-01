from django.http import HttpResponse
from django.shortcuts import render 
from apps.home.models import *
from django.db.models import F, Q
from apps.home.views.functions import *

def org_dashboard(request):
    context = {}
    context["nbr_etablisement"] = Etablisment.objects.filter().count()
    context["nbr_divisions"] = Division.objects.filter().count()
    context["nbr_equipes"] = Equipe.objects.filter().count()
    context["nbr_researcher"] = Researcher.objects.filter().count()
    return render(request , "home/organisation/1-dashboard.html" , context)


def org_etablisements(request):
    return render(request, 'home/organisation/filter_etablisements.html')

def divisions_of_etablisement(request,pk):
    return render(request, 'home/organisation/filter_divisions.html')


def org_divisions(request):
    return render(request , 'home/organisation/3-1org-divisions.html')

def equipes_of_division(request, pk):
    return render(request , 'home/organisation/3-2equipes-divisions.html')


def chercheurs_of_division(request):
    return render(request ,'home/organisation/3-3cher-division.html')
    
def org_equipes(request):
    return render(request , 'home/organisation/4-org-equipes.html')
    # return HttpResponse('equipes of an organisations')

def members_of_equipe(request):
    pass