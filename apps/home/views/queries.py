from __future__ import division
from django.db.models import Q,F

from ..models import *


# etablisement
def eta_divs(eta_id):
    return Division.objects.filter(etablisment=eta_id)
def eta_equipes(eta_id):
    return Equipe.objects.filter(division__etablisment=eta_id)
def eta_chers(eta_id):
    return Researcher.objects.filter(Q(division__etablisment__id=eta_id) | Q(equipe__division__etablisment__id=eta_id) | Q(equipe_researchers__division__etablisment__id=eta_id) | Q(etablisment__id=eta_id))

# dashboard
def top_10_researchers_citations_eta(eta_id):
    _list = list(eta_chers(eta_id).order_by(F("citations").desc()))[:5]
    return _list

def top_10_researchers_hindex_eta(eta_id):
    _list = list(eta_chers(eta_id).order_by(F("h_index").desc()))[:5]
    return _list

def top_10_researchers_i10_index_eta(eta_id):
    _list = list(eta_chers(eta_id).order_by(F("i10_index").desc()))[:5]
    return _list



# divisions
def div_equipes(div_id):
    return Equipe.objects.filter(division=div_id)
def div_chers(div_id):
    return Researcher.objects.filter(division=div_id)

# equipe
def equipe_chers(equipe_id):
    return Researcher.objects.filter(Q(equipe_researchers=equipe_id) | Q(equipe=equipe_id))