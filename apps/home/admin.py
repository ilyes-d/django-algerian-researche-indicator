from django import forms
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from django.core.exceptions import ValidationError
from apps.home.models import *


class UserCreationForm(forms.ModelForm):
    """
    """
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(
        label='Password Confirmation', widget=forms.PasswordInput)

    class Meta:
        model = Researcher
        fields = ('email', 'first_name', 'last_name', 'speciality',
                  'grade', 'google_scholar_account')

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
                    'grade', 'linkedin_account', 'google_scholar_account', 'equipe_researchers')
    list_filter = ('is_staff',)
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Personal info', {'fields': ('first_name', 'last_name', 'speciality',
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
