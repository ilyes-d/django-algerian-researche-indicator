from django.http import Http404, HttpResponse
from django.shortcuts import redirect
from apps.home.models import Etablisment 
from apps.home.views.fcts import *

def only_chef_eta(function):
    def wrapper(request):
        if not is_chef_eta(request):
            raise HttpResponse('you don\'t have access')
        return function(request)
    return wrapper

def is_superuser(function):
    def wrapper(request):
        if not request.user.is_superuser:
            raise Http404('this page only for super user')
        return function(request)    
    return wrapper 

  
def redirect_logged_in_user(func):
    def wrapper(request):
        if request.user.is_authenticated:
            if user_role(request) == 'membre':
                return redirect("/profile/")
            return redirect("/"+str(user_role(request)+"/dashboard"))
        else:
            return func(request)
    return wrapper

def is_chef_eta(request):
    try:
        Etablisment.objects.get(chef_etablisement=request.user.id)
        return True
    except Etablisment.DoesNotExist:
        return False

def is_chef_div(request):
    try:
        Division.objects.get(chef_div=request.user.id)
        return True
    except Division.DoesNotExist:
        return False

def is_chef_equipe(request):
    try:
        Equipe.objects.get(chef_equipe=request.user.id)
        return True
    except Equipe.DoesNotExist:
        return False

def is_profile_in_your_eta(request,pk):
    eta_id = Etablisment.objects.get(chef_etablisement=request.user.id)
    try:
        pk_eta = Etablisment.objects.get(division__chef_div=pk).id
        if eta_id == pk_eta:
            return True
        return False
    except Etablisment.DoesNotExist :
        pk_eta = None
    try:
        pk_eta = Etablisment.objects.get(division__equipe__researcher=pk).id
        if eta_id == pk_eta:
            return True
        return False
    except Etablisment.DoesNotExist :
        pk_eta = None
    if pk_eta==None:
        return False        
    
def is_profile_in_your_div(request,pk):
    div_id = Division.objects.get(chef_div=request.user.id).id
    try:
        profile_div = Division.objects.get(equipe__researcher=pk).id
        if profile_div == div_id :
            return True
        return False
    except Division.DoesNotExist :
        profile_div = None
    try:
        profile_div=Division.objects.get(equipe__chef_equipe=pk).id
        if profile_div == div_id :
            return True
        return False
    except Division.DoesNotExist :
        profile_div = None
    if profile_div==None:
        return False

def is_profile_in_your_equipe(request,pk):
    equipe_id = Equipe.objects.get(chef_equipe=request.user.id).id
    try:
        profile_equipe = Equipe.objects.get(researcher=pk).id
        if profile_equipe == equipe_id:
            return True
        return False
    except Equipe.DoesNotExist :
        profile_equipe = None
    try:
        profile_equipe=Equipe.objects.get(chef_equipe=pk).id
        if profile_equipe == equipe_id :
            return True
        return False
    except Equipe.DoesNotExist :
        profile_equipe = None
    if profile_equipe==None:
        return False
        
    
def who_can_see_profile(function):
    """
    chef eta can see all his eta researchers
    chef division can see all his divs researchers
    chef equipe can see the members of his equipe
    everyone can see his profile 
    """  
    def wrapper(request,pk):
            if not request.user.is_authenticated :
                raise Http404("not authenticated ")
            if not request.user.is_superuser:
                if request.user.id == pk:
                    return function(request,pk)
                if is_chef_eta(request):
                    if is_profile_in_your_eta(request,pk):
                        return function(request,pk)
                    raise Http404("you don't have access")
                        # HttpResponse("the user you requested is out of your div")
                if is_chef_div(request):
                    if is_profile_in_your_div(request,pk):
                        return function(request,pk)
                    raise Http404("you don't have access")
                        # HttpResponse("this user out of your division ")
                if is_chef_equipe(request):
                    if is_profile_in_your_equipe(request,pk):
                        return function(request,pk)
                    raise Http404("you don't have access")
                        # HttpResponse("this user out of your equipe ")
                raise Http404("you don't have access")
                # HttpResponse('you arent a part of any etablisement or div or equipe')
            return function(request,pk)
    return wrapper
    
    
    
    
    
    
    
    
    
    