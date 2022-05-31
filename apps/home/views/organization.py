from django.shortcuts import render 
from apps.home.models import *

def org_dashboard(request):
    context = {}
    context["nbr_etablisement"] = Etablisment.objects.filter().count()
    context["nbr_divisions"] = Division.objects.filter().count()
    context["nbr_equipes"] = Equipe.objects.filter().count()
    context["nbr_researcher"] = Researcher.objects.filter().count()
    return render(request , "home/organisation/dashboard.html" , context)

def org_etablisements(request):
    return render(request, 'home/organisation/filter_etablisements.html')

def divisions_of_etablisement(request,pk):
    return render(request, 'home/organisation/filter_divisions.html')


def org_divisions(request):
    pass

def equipes_of_division(request, pk):
    pass

def org_equipes(request):
    pass

def members_of_equipe(request):
    pass