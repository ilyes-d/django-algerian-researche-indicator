from django import forms
from apps.home.admin import UserCreationForm
from apps.home.models import Researcher
class LoginForm(forms.Form):
    email = forms.EmailField(widget=forms.EmailInput(attrs={"placeholder": "Email","class": "form-control"}))
    password = forms.CharField(widget=forms.PasswordInput( attrs={ "placeholder": "Password", "class": "form-control"}))


class SignUpForm(UserCreationForm):
    first_name = forms.CharField(widget=forms.TextInput( attrs={ "placeholder": "Entre votre Prenom", "class": "form-control"}))
    last_name = forms.CharField(widget=forms.TextInput(attrs={ "placeholder": "Entre votre Nom", "class": "form-control" } ))
    email = forms.EmailField(widget=forms.EmailInput(attrs={"placeholder": "Entre votre Email","class": "form-control"}))
    speciality = forms.CharField(widget=forms.TextInput(attrs={"placeholder": "Entre votre Specialiy","class": "form-control"}))
    grade = forms.CharField(widget=forms.TextInput(attrs={"placeholder": "Entre votre Grade ","class": "form-control"}))
    google_scholar_account = forms.URLField(widget=forms.URLInput(attrs={"placeholder":"https://scholar.google.com/citations", "class":"form-control"}))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={"placeholder": "Password","class": "form-control"}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={"placeholder": "Confirm Password","class": "form-control"}))
    class Meta:
        model = Researcher
        fields = ('email', 'first_name','last_name','speciality','grade','google_scholar_account','password1', 'password2',)
        