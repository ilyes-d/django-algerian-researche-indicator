from ..models import *
import django_filters as filter
from django import forms
from django.shortcuts import render 


class DivisionFilter(filter.FilterSet):
    wilaya = filter.ModelChoiceFilter(field_name='etablisment__location',queryset=Location.objects.all(),widget=forms.Select(attrs={"class": "form-select"}),initial='Choisi le jasd')
    etablisment = filter.ModelChoiceFilter(field_name='etablisment',queryset=Etablisment.objects.all(),widget=forms.Select(attrs={"class": "form-select"}))
    class Meta:
        model = Division
        fields = [
            # 'etablisment'
            ]


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

class EtablismentFilter(filter.FilterSet):
    location = filter.ModelChoiceFilter(widget=forms.Select(attrs={"placeholder": "Choisir un wilaya", "class": "form-select"}),queryset=Location.objects.all())
    class Meta:
        model = Etablisment
        fields = ['location']
        # form = EtablisementForm
      
# class DivisionFilter(django_filters.FilterSet):
#     class Meta:
#         model = Division
#         fields = '__all__'
def eta(request):
    return Etablisment.objects.all()
# class EquipeFilter(django_filters.FilterSet):
#     etablisement = django_filters.ModelChoiceFilter(queryset=eta)
#     class Meta:
#         model = Equipe
#         fields = ['nom','etablisement']
# # def load_etas(request):

# def etablisement_list(request):
#     # f = EtablismentFilter(request.GET)
#     # f = DivisionFilter(request.GET)
#     f = EquipeFilter(request.GET)
#     return render(request, 'empty.html' , {'filter':f})




        
