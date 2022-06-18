


from pyexpat.errors import messages
from django.shortcuts import redirect, render

from apps.home.forms import EtablismentForm


def creat_Etablisment_views(request):
    form =EtablismentForm(data=request.POST)
    if request.method =="POST":     
        if form.is_valid() :
             form.save()
             return redirect("org-etas-liste")
        return render(request,"crud/creatEtablisment.html",{"form":form})

    else:
           form=EtablismentForm
           return render(request,'crud/creatEtablisment.html',{"form":form})