from __future__ import division
from dataclasses import fields
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

class CherFitler(django_filters.FilterSet):
    # eta = django_filters.ModelChoiceFilter()
    class Meta:
        model = Researcher
        fields=['first_name']

# for chef div 
def search(request):
    equipe_list = Equipe.objects.all()
    # equipe_list = Equipe.objects.filter(division,)
    equipe_filter = EquipeFiter(request.GET , queryset=equipe_list)
    chers_list = Researcher.objects.filter(equipe_researchers__division__etablisment__location=16)
    cher_filter = CherFitler(request.GET, queryset=chers_list)
    return render(request , 'empty.html',{'filter':cher_filter})

