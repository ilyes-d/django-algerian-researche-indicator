from multiprocessing import context
from django.shortcuts import redirect,render 
from ..models import *
from ..decorators import *

@who_can_see_profile
def researcher_profile(request, pk):
    context= {
        'researcher': Researcher.objects.filter(id = pk)
    }
    return render(request,'home/profile.html',context)
    