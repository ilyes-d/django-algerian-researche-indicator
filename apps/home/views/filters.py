from __future__ import division
from dataclasses import fields

from django.db import DJANGO_VERSION_PICKLE_KEY
from ..models import *
import django_filters
from django import forms
from django.shortcuts import render 


class EtablisementForm(forms.ModelForm):
    
    class Meta:
        model= Etablisment
        fields = ['nom','location']
        
    def __init__(self,*args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['nom'].queryset = Etablisment.objects.all()
        self.fields['location'].queryset = Location.objects.all()
        
def divs_of_eta(request):
    return Division.objects.all()

class EtablismentFilter(django_filters.FilterSet):
    # nom = django_filters.MultipleChoiceFilter
    division = django_filters.ModelChoiceFilter(queryset=divs_of_eta)
    class Meta:
        model = Etablisment
        fields = ['nom','location','division']
        # form = EtablisementForm
      
class DivisionFilter(django_filters.FilterSet):
    class Meta:
        model = Division
        fields = '__all__'
def eta(request):
    return Etablisment.objects.all()
class EquipeFilter(django_filters.FilterSet):
    etablisement = django_filters.ModelChoiceFilter(queryset=eta)
    class Meta:
        model = Equipe
        fields = ['nom','etablisement']
# def load_etas(request):

def etablisement_list(request):
    # f = EtablismentFilter(request.GET)
    # f = DivisionFilter(request.GET)
    f = EquipeFilter(request.GET)
    return render(request, 'empty.html' , {'filter':f})
