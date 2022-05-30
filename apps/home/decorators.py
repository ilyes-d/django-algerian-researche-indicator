from django.http import Http404 , HttpResponse
from django.shortcuts import redirect, render
from apps.home.models import Etablisment 
from apps.home.views.fcts import *

def is_chef_eta(function):
    def wrapper(request):
        if not Etablisment.objects.filter(chef_etablisement=request.user.id):
            return HttpResponse('you don\'t have access')
        return function(request)
    return wrapper


def is_superuser(function):
    def wrapper(request):
        if not request.user.is_superuser:
            return HttpResponse('this page only for super user')
        return function(request)    
    return wrapper 

def is_chef_division(request):
    pass


def redirect_logged_in_user(func):
    def wrapper(request):
        if request.user.is_authenticated:
            return redirect("/"+str(user_role(request)+"/dashboard"))
        else:
            return func(request)
    return wrapper
