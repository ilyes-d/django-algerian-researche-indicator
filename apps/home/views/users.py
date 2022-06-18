from django.http import JsonResponse
from django.shortcuts import render
from ..models import *
from ..decorators import *
from .functions import *
from django.contrib.auth.decorators import login_required
from django.template import loader



@login_required(login_url="/login/")
def index(request):
    context = {'segment': 'index'}
    html_template = loader.get_template('home/index.html')
    return HttpResponse(html_template.render(context, request))



@who_can_see_profile
def researcher_profile(request, pk):
    context = {}
    try:
        researcher = Researcher.objects.get(id = pk)
    except Researcher.DoesNotExist:
        return render(request,'404.html',context)
    context['researcher'] = researcher
    return render(request,'home/profile.html',context)
        