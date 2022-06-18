from __future__ import division
from cProfile import label
from dataclasses import fields
from tabnanny import verbose
from django.http import Http404

from requests import request
from apps.home.templatetags.tag import chef_etablisement

from apps.home.views.filters import EtablisementForm
from apps.home.views.functions import query_all_etablisements
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

def div(request):
    # if request is None:
    #     raise Http404('hello')
        # return Division.objects.none()
    # etablisment = request.user.etablisment
    # return etablisment.division_set.all()
    eta = request.user.etablisment
    return eta.division_set.all()

class CherFitler(django_filters.FilterSet):
    f = django_filters.CharFilter(field_name='first_name',lookup_expr='contains',label='fd')
    
    # first_name = django_filters.ModelChoiceFilter(field_name='first_name',queryset=Researcher.objects.values_list('first_name',flat=True))
    # equipe_researchers__division__etablisment = django_filters.CharFilter(field_name='etablisment')
    etab = django_filters.ModelChoiceFilter(field_name='equipe_researchers__division__etablisment__location',queryset=Location.objects.all(),label='ha')
    etab = django_filters.ModelChoiceFilter(field_name='equipe_researchers__division__etablisment',queryset=Etablisment.objects.all(),label='df')
    # division = django_filters.ModelChoiceFilter(queryset=div)
    field_labels ={
        'equipe_researchers__division__etablisment': 'haha',
    }
    
    class Meta:
        model = Researcher
        fields=['first_name',
                # 'equipe_researchers__division__etablisment'
                ]

# for chef div 
def search(request):
    if request.method == 'GET':
        chers_list = Researcher.objects.all()
        cher_filter = CherFitler(request.GET, queryset=chers_list)
    
    researchers = Researcher.objects.all()
    
    return render(request , 'empty.html',{'filter':cher_filter, 'researchers':researchers })
    
    equipe_list = Equipe.objects.all()
    # equipe_list = Equipe.objects.filter(division,)
    # equipe_filter = EquipeFiter(request.GET , queryset=equipe_list)
    # chers_list = Researcher.objects.filter(equipe_researchers__division__etablisment__location=16)
    
    
    

