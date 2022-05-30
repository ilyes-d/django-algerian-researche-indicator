from atexit import register
from django import template
from apps.home.models import *
register = template.Library()


@register.filter
def chef_etablisement(user):
    if Etablisment.objects.filter(chef_etablisement__id=user.id):
        return True
    return False


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
    if (not chef_etablisement(user) and not chef_division(user) and not chef_equipe(user)):
        return True
    return False
