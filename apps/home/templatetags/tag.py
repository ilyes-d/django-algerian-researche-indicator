from atexit import register
from django import template
from apps.home.models import *
from ..decorators import is_chef_eta
register = template.Library()


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
