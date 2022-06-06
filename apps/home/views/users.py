from multiprocessing import context
from django.shortcuts import redirect,render 
from ..models import *
from ..decorators import *

@who_can_see_profile
def researcher_profile(request, pk):
    context = {}
    try:
        researcher = Researcher.objects.get(id = pk)
    except Researcher.DoesNotExist:
        return render(request,'404.html',context)
    context['researcher'] = researcher 
    return render(request,'home/profile.html',context)
    
def eta_dash_id(request,pk):
    context = {}
    return render(request , 'home/eta/dashboard.html',context)