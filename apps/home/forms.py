


from django import forms
from django.forms import ModelForm
from apps.home.models import Division, Etablisment, Location, Researcher


class EtablismentForm  (ModelForm):
      nom=forms.CharField(widget=forms.TextInput( attrs={ "placeholder": "Entre le nom de l'établissement", "class": "form-control"}))
    #   logo=
      site_web= forms.URLField(widget=forms.URLInput(attrs={"placeholder":"Le lien du site de l'établissement", "class":"form-control"}))
      location= forms.ModelChoiceField(queryset=Location.objects.all(), empty_label="Enter la Wilaya de l'etablissment" )
      chef_etablisement= forms.ModelChoiceField(queryset=Researcher.objects.all(), empty_label="Le chef de l'etablissment" )
    #   long_nom=
      long_nom=forms.CharField(widget=forms.TextInput( attrs={ "placeholder": "Entre le nom complet de l'établissement", "class": "form-control"}))
      class Meta:
          model = Etablisment
          fields = ('nom','site_web','location','chef_etablisement','long_nom')


class DivisionForm  (ModelForm):
      nom=forms.CharField(widget=forms.TextInput( attrs={ "placeholder": "Entre le nom de la division", "class": "form-control"}))
    #   logo=
      site_web= forms.URLField(widget=forms.URLInput(attrs={"placeholder":"Le lien du site de la division", "class":"form-control"}))
      etablisment= forms.ModelChoiceField(queryset=Etablisment.objects.all(), empty_label="Enter  l'établissement de la division " )
      chef_div= forms.ModelChoiceField(queryset=Researcher.objects.all(), empty_label="Le chef de l'etablissment" )
    #   long_nom=
      long_nom=forms.CharField(widget=forms.TextInput( attrs={ "placeholder": "Entre le nom complet de la division", "class": "form-control"}))
      class Meta:
          model = Division
          fields = ('nom','site_web','etablisment','chef_div','long_nom')