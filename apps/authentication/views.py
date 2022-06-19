from multiprocessing import context
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from .forms import LoginForm
from apps.home.views.fcts import *
from apps.home.decorators import *
from django.contrib import messages
from apps.home.admin import UserCreationForm
from apps.home.views.queries import *

@redirect_logged_in_user
def login_view(request):
    form = LoginForm(request.POST or None)
    msg = None
    if request.method == "POST":
        if form.is_valid():
            email = form.cleaned_data.get("email")
            password = form.cleaned_data.get("password")
            user = authenticate(email=email, password=password)
            if user is not None:
                login(request, user)
                if user_role(request) == 'membre':
                    return redirect('profile/user='+request.user.id)
                return redirect_users_after_login(request)
            else:
                msg = 'les informations d\'identification sont invalides'
        else:
            msg = 'Error validating the form'

    return render(request, "accounts/login.html", {"form": form, "msg": msg})


@redirect_logged_in_user
def register_user(request):
    context = {}
    msg = None
    success = False
    context['wilayas'] =all_wilayas()
    context['etas'] = all_etas()
    context['divs'] = all_divs()
    context['equipes']=all_equipes()
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            email = form.cleaned_data.get("email")
            raw_password = form.cleaned_data.get("password1")
            equipe_id = request.POST.get('equipe_id')
            user = authenticate(email=email, password=raw_password)
            user.equipe_id= equipe_id 
            user.is_authorized = False
            user.save()
            if user is not None :
                login(request, user)
                if user_role(request) == 'membre':
                    return redirect('researcher_profile', pk=user.id)
                return redirect("/"+str(user_role(request))+"/dashboard")
            else:
                msg = 'Invalid credentials'   
            msg = 'User created - please <a href="/login">login</a>.'
            success = True

        else:
            msg = 'Form is not valid'
    else:
        form = UserCreationForm()
    context['form'] =form
    context['msg'] = msg
    context['success'] = success
    # return render(request, "accounts/register.html", {"form": form, "msg": msg, "success": success})
    return render(request, "accounts/register.html", context)


def see_user_data(request):
    context = {}
    context['wilayas'] = Location.objects.all()
    context['etas'] = Etablisment.objects.all()
    return render(request , 'empty.html',context)