from atexit import register
from django import template
from apps.home.admin import EtablisementAdmin
from apps.home.models import *
# from ..decorators import is_chef_div, is_chef_equipe, is_chef_eta
from ..views.is_cdt import *
from django.db.models import *
register = template.Library()

@register.filter
def get_item(dict,key):
    return dict[key]

@register.filter
def cher_info(cher):
    context = {}
    context["eta"] = Etablisment.objects.get(division__equipe__researcher=cher.id)
    context["equipe"] = Equipe.objects.get(researcher=cher.id)
    context["div"] = Division.objects.get(equipe__researcher=cher.id)
    return context
    

@register.filter
def user_role(user):
    roles = []
    if is_chef_eta(user):
        print("this is so boring")
        roles.append(" ".join(["Chef Etablisement",Etablisment.objects.get(chef_etablisement=user.id).nom]))
    if is_chef_div(user):
        roles.append(" ".join(["Chef Division",Division.objects.get(chef_div=user.id).nom]))
    if is_chef_equipe(user):
        roles.append(" ".join(["Chef Equipe",Equipe.objects.get(chef_equipe=user.id).nom]))
    if is_equipe_member(user):
        roles.append(" ".join(["membre de l'equipe",Equipe.objects.get(researcher=user.id).nom]))
    return ','.join(roles)

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
    else:
        return Equipe.objects.get(researcher=user.id).id

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
def equipe_member(user):
    if user.equipe_researchers == None:
        return False
    return True
        

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
def cher_eta(cher):
    if is_chef_eta(cher):
        return Etablisment.objects.get(chef_etablisement=cher.id)
    if is_chef_div(cher):
        return Etablisment.objects.get(division__chef_div=cher.id)
    elif is_equipe_member(cher):
        return  Etablisment.objects.get(division__equipe__researcher=cher.id)

@register.filter
def cher_equipe(cher):
    if is_chef_equipe(cher):
        return Equipe.objects.get(chef_equipe=cher.id)
    elif is_equipe_member(cher):
        return Equipe.objects.get(researcher=cher.id)

@register.filter
def equipe_request(cher):
    return Equipe.objects.get(id=cher.equipe_id)

@register.filter
def eta_request(cher):
    return Etablisment.objects.get(division__equipe=cher.equipe_id)

@register.filter
def div_request(cher):
    return Division.objects.get(equipe=cher.equipe_id)
    
@register.filter
def cher_div(cher):
    if is_chef_div(cher):
        return Division.objects.get(chef_div=cher.id)


