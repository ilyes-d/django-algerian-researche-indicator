<<<<<<< HEAD
from django.shortcuts import get_object_or_404, redirect, render
from apps.home.views.fcts import *
from apps.home.decorators import *


def dash_equipe(request):
    context = Dash_Equipe_calc(get_equipe_id(request))
    return render (request,'home/equipe/dashboard.html',context) 


def dash_divisions(request,pk):
    context = Dash_Equipe_calc(pk)
    return render (request,'DashDivision.html',context)
=======
def equipe_dashboard(request):
    pass
>>>>>>> 37a5d509b0a1e214a0eb3a10406d8c2ad5edbf23
