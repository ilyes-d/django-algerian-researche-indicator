from __future__ import division
from django.db.models import Q,F

from ..models import *

# org     
    

# etablisement
def eta_divs(eta_id):
    return Division.objects.filter(etablisment=eta_id)
def eta_equipes(eta_id):
    return Equipe.objects.filter(division__etablisment=eta_id)
def eta_chers(eta_id):
    return Researcher.objects.filter(Q(division__etablisment__id=eta_id) | Q(equipe__division__etablisment__id=eta_id) | Q(equipe_researchers__division__etablisment__id=eta_id) | Q(etablisment__id=eta_id))


# Top
def top_5_researchers_citations(chers):
    _list = list(chers.order_by(F("citations").desc()))[:5]
    return _list

def top_5_researchers_hindex(chers):
    _list = list(chers.order_by(F("h_index").desc()))[:5]
    return _list

def top_5_researchers_i10_index(chers):
    _list = list(chers.order_by(F("i10_index").desc()))[:5]
    return _list



# divisions
def div_equipes(div_id):
    return Equipe.objects.filter(division=div_id)

def div_chers(div_id):
    return Researcher.objects.filter(Q(division=div_id)|Q(equipe_researchers__division=div_id))

# equipe
def equipe_chers(equipe_id):
    return Researcher.objects.filter(Q(equipe_researchers=equipe_id) | Q(equipe=equipe_id))


def all_wilayas():
    return Location.objects.all()
def all_etas():
    return Etablisment.objects.all()
def all_divs():
    return Division.objects.all()
def all_equipes():
    return Equipe.objects.all()