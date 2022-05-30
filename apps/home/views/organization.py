from django.shortcuts import render 

def dashboard(request):
    return render(request , "home/organization/dashboard.html")

def etablisements(request):
    return render(request)