from atexit import register
from django import template
from apps.home.models import *
from ..decorators import is_chef_div, is_chef_equipe, is_chef_eta
from django.db.models import *
register = template.Library()


@register.filter
def user_role(user):
    if is_chef_eta(user):
        return " ".join(["Chef Etablisement",Etablisment.objects.get(chef_etablisement=user.id).nom])
    if is_chef_div(user):
        return " ".join(["Chef Division",Division.objects.get(chef_div=user.id).nom])
    if is_chef_equipe(user):
        return " ".join(["Chef Equipe",Equipe.objects.get(chef_equipe=user.id).nom])
    return " ".join(["membre de l'equipe",Equipe.objects.get(researcher=user.id).nom])

@register.filter
def chef_etablisement(user):
    if Etablisment.objects.filter(chef_etablisement__id=user.id):
        return True
    return False

@register.filter
def eta_id(user):
    if is_chef_eta(user):
        return Etablisment.objects.get(chef_etablisement=user.id).id

@register.filter
def div_id(user):
    if is_chef_div(user):
        return Division.objects.get(chef_div=user.id).id

@register.filter 
def equipe_id(user):
    if is_chef_equipe(user):
        return Equipe.objects.get(chef_equipe=user.id).id

@register.filter
def chef_division(user):
    if Division.objects.filter(chef_div__id=user.id):
        return True
    return False

@register.filter
def chef_equipe(user):
    if Equipe.objects.filter(chef_equipe__id=user.id):
        return True
    return False

@register.filter
def membre_simple(user):
    if (not chef_etablisement(user) and not chef_division(user) and not chef_equipe(user) and not user.is_superuser):
        return True
    return False

@register.simple_tag
def count_percentage(total,value):
    if total == 0:
        return "0"
    return str(round(value*100/total , 2)) +'%'


@register.filter
def get_eta(user):
    print(user)
    return Etablisment.objects.filter(Q(division__equipe__researcher=user.id) | Q(division__chef_div=user.id) | Q(chef_etablisement=user.id)|Q(division__equipe__chef_equipe=user.id))[0]


