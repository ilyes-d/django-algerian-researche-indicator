from multiprocessing import context
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from .forms import LoginForm
from apps.home.views.fcts import *
from apps.home.decorators import *
from django.contrib import messages
from apps.home.admin import UserCreationForm


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
                msg = 'Invalid credentials'
        else:
            msg = 'Error validating the form'

    return render(request, "accounts/login.html", {"form": form, "msg": msg})


@redirect_logged_in_user
def register_user(request):
    msg = None
    success = False

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            email = form.cleaned_data.get("email")
            raw_password = form.cleaned_data.get("password1")
            google_scholar_account = form.cleaned_data.get("google_scholar_account")
            user = authenticate(email=email, password=raw_password , google_scholar_account = google_scholar_account)
            if user is not None :
                login(request, user)
                if user_role(request) == 'membre':
                    return redirect('/profile/')
                return redirect("/"+str(user_role(request))+"/dashboard")
            else:
                msg = 'Invalid credentials'   
            msg = 'User created - please <a href="/login">login</a>.'
            success = True

        else:
            msg = 'Form is not valid'
    else:
        form = UserCreationForm()

    return render(request, "accounts/register.html", {"form": form, "msg": msg, "success": success})


def see_user_data(request):
    context = {}
    user = Researcher.objects.get(id=request.user.id)
    user.first_name = "ana howa"
    user.save()
    context["first_name"] = request.user.first_name
    context["userd"] = user
    return render(request , 'empty.html',context)