from multiprocessing import context
from django.shortcuts import redirect,render 
from ..models import *
from ..decorators import *
from .functions import *






@who_can_see_profile
def researcher_profile(request, pk):
    context = {}
    try:
        researcher = Researcher.objects.get(id = pk)
    except Researcher.DoesNotExist:
        return render(request,'404.html',context)
    
    context['researcher'] = researcher
    # researcher.
    researcher_gs = serpapi_author(researcher.get_google_id())
    print(researcher.citations)
    print("second")
    print(researcher_gs["cited_by"]["table"][0]["citations"]["all"])
    researcher.citations = researcher_gs["cited_by"]["table"][0]["citations"]["all"]
    researcher.save()
    
    return render(request,'home/profile.html',context)
    
    
    

def eta_dash_id(request,pk):
    context = {}
    return render(request , 'home/eta/dashboard.html',context)