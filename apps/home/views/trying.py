from __future__ import division
from ..models import *
import django_filters
from django import forms
from django.shortcuts import render 


class EquipeFiter(django_filters.FilterSet):
    # nom = django_filters.CharFilter(lookup_expr='icontains')
    nom = Equipe.objects.all()
    division = Division.objects.all()
    class Meta :
        model = Equipe
        fields = ['nom','division']


# for chef div 
def search(request):
    equipe_list = Equipe.objects.all()
    # equipe_list = Equipe.objects.filter(division,)
    equipe_filter = EquipeFiter(request.GET , queryset=equipe_list)
    return render(request , 'empty.html',{'filter':equipe_filter})

