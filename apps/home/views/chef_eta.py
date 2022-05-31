from django.forms import inlineformset_factory
from django.shortcuts import get_object_or_404, redirect, render
from apps.home.models import *
from apps.home.forms import *
from django.contrib import messages
from django.contrib.auth import *
from apps.home.decorators import *
from apps.home.views.fcts import *
from apps.home.decorators import *


@is_chef_eta
def dash_etablisemnt(request):
    context = Dash_Eta_calc(get_etablisement_id(request))
    return render (request,'home/etablisement/dashboard.html',context)  
 

@is_superuser
def dash_etablisemnts(request,pk):
    context = Dash_Eta_calc(pk)
    return render (request,'dashboardEta.html',context)




  