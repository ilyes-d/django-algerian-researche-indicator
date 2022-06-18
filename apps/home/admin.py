from django import forms
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from django.core.exceptions import ValidationError
from apps.home.models import *
from urllib.parse import urlparse
from apps.home.views.fcts import *


class UserCreationForm(forms.ModelForm):
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
        fields = ('email', 'first_name', 'last_name', 'speciality','grade', 'google_scholar_account')
        
    # def clean_google_scholar_account(self):
    #     cleaned_data = super().clean()
    #     google_scholar_account = cleaned_data.get("google_scholar_account") 
    #     domain = urlparse(google_scholar_account).netloc
    #     if not domain == 'scholar.google.com' :
    #         self.add_error('google_scholar_account' , "format du compte google scholar  fournit non valide")
    #     elif not check_gs_id(get_gs_id(google_scholar_account)):
    #         raise forms.ValidationError(" Le compte google scholar n\'est pas valide , prier de le vérifier !")
        

    def clean_password2(self):
        password1 = self.cleaned_data["password1"]
        password2 = self.cleaned_data["password2"]
        if password1 and password2 and password1 != password2:
            raise ValidationError("passwords don't match ")
        return password2

    def save(self, commit=True):
        user = super().save(commit=False)
        
        user.set_password(self.cleaned_data["password1"])
        
        if commit:
            print("fdsa :")
            print(user.google_scholar_account)
            user.save()
        return user


class UserChangeForm(forms.ModelForm):
    password = ReadOnlyPasswordHashField()

    class Meta:
        model = Researcher
        fields = ('email', 'first_name', 'last_name',
                  'speciality', 'grade', 'google_scholar_account', 'is_active', 'is_staff', 'equipe_researchers')


class UserAdmin(BaseUserAdmin):
    form = UserChangeForm
    add_form = UserCreationForm
    list_display = ('__str__', 'email', 'first_name', 'is_staff', 'last_name', 'speciality',

                    # 'citations','h_index','i10_index',"graph_citation",'nbr_pubs','graph_pub',

                    "h_index",

                    'grade', 'linkedin_account', 'google_scholar_account', 'equipe_researchers')
    list_filter = ('is_staff',)
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Personal info', {'fields': ('first_name', 'last_name', 'speciality',
                                      'citations','h_index','i10_index',"graph_citations",'nbr_pubs','graph_pub',
                                      'grade', 'linkedin_account', 'google_scholar_account',)}),
        ('Permissions', {'fields': ('is_active', 'is_staff',
         'is_superuser', 'groups', 'user_permissions',)}),
        ('Relations', {'fields': ('equipe_researchers',)}),
    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'first_name', 'last_name', 'speciality', 'grade', 'linkedin_account', 'google_scholar_account', 'equipe_researchers', 'password1', 'password2'),
        }),
    )
    search_fields = ('email',)
    ordering = ('date_joined',)


admin.site.register(Researcher, UserAdmin),
admin.site.register(Location),
admin.site.register(Etablisment),
admin.site.register(Division),
admin.site.register(Equipe),
