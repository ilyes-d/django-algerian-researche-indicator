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