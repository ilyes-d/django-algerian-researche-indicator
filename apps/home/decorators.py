from django.http import Http404, HttpResponse
from django.shortcuts import redirect
from apps.home.models import Etablisment 
from apps.home.views.fcts import *
from .views.is_cdt import *

def redirect_logged_in_user(func):
    def wrapper(request):
        if request.user.is_authenticated:
            if request.user.is_superuser :
                return redirect('org-carte')
            if is_chef_eta(request.user):
                return redirect('eta-dash',eta_id=Etablisment.objects.get(chef_etablisement=request.user.id).id)
            if is_chef_div(request.user):
                return redirect('div-dash')
            if is_chef_equipe(request.user):
                return redirect('equipe-dash')
            if user_role(request) == 'membre':
                return redirect("researcher_profile",pk =request.user.id)
        else:
            return func(request)
    return wrapper    

def only_chef_eta(function):
    def wrapper(request):
        if not is_chef_eta(request.user):
            raise HttpResponse('you don\'t have access')
        return function(request)
    return wrapper

def is_superuser(function):
    def wrapper(request):
        if not request.user.is_superuser:
            raise Http404('this page only for super user')
        return function(request)    
    return wrapper 

# this is only for who can see profile 
    
def who_can_see_profile(function):
    """
    detect the identity of who request a profile 
    chef eta can see all his eta researchers
    chef division can see all his divs researchers
    chef equipe can see the members of his equipe
    everyone can see his profile 
    """  
    def wrapper(request,pk):
            if not request.user.is_authenticated :
                return redirect("/login/")
            if not request.user.is_superuser:
                if request.user.id == pk:
                    return function(request,pk)
                if is_chef_eta(request.user):
                    if is_profile_in_your_eta(request,pk):
                        return function(request,pk)
                    raise Http404("you don't have access chef eta")
                        # HttpResponse("the user you requested is out of your div")
                if is_chef_div(request.user):
                    if is_profile_in_your_div(request,pk):
                        return function(request,pk)
                    raise Http404("you don't have access")
                        # HttpResponse("this user out of your division ")
                if is_chef_equipe(request.user):
                    if is_profile_in_your_equipe(request,pk):
                        return function(request,pk)
                    raise Http404("you don't have access")
                        # HttpResponse("this user out of your equipe ")
                ds = request.user.id == pk
                raise Http404("you don't have access member"+str(type(request.user.id))+str(type(pk))+str(ds))
            return function(request,pk)
    return wrapper    
    
def divsions_request(function):
    def wrapper(request,pk):
        
        pass
    return wrapper
    