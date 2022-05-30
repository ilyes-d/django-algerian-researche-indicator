from django.shortcuts import render 

def dashboard(request):
    return render(request , "home/organisation/dashboard.html")

def etablisements(request):
    return render(request)