"""
a True\False based functions,
"""
from ..models import *

def is_chef_eta(user):
    try:
        Etablisment.objects.get(chef_etablisement=user.id)
        return True
    except Etablisment.DoesNotExist:
        return False
    
def is_chef_div(user):
    try:
        Division.objects.get(chef_div=user.id)
        return True
    except Division.DoesNotExist:
        return False

def is_chef_equipe(user):
    try:
        Equipe.objects.get(chef_equipe=user.id)
        return True
    except Equipe.DoesNotExist:
        return False

def is_equipe_member(user):
    try:
        Equipe.objects.get(researcher=user.id)
        return True
    except Equipe.DoesNotExist:
        return False
    
def is_profile_in_your_eta(request,pk):
    eta_id = Etablisment.objects.get(chef_etablisement=request.user.id).id
    try:
        pk_eta = Etablisment.objects.get(division__chef_div=pk).id
        if eta_id == pk_eta:
            return True
        return False
    except Etablisment.DoesNotExist :
        pk_eta = None
    try:
        pk_eta = Etablisment.objects.get(division__equipe__researcher=pk).id
        if eta_id == pk_eta:
            return True
        return False
    except Etablisment.DoesNotExist :
        pk_eta = None
    if pk_eta==None:
        return False        
    
def is_profile_in_your_div(request,pk):
    div_id = Division.objects.get(chef_div=request.user.id).id
    try:
        profile_div = Division.objects.get(equipe__researcher=pk).id
        if profile_div == div_id :
            return True
        return False
    except Division.DoesNotExist :
        profile_div = None
    try:
        profile_div=Division.objects.get(equipe__chef_equipe=pk).id
        if profile_div == div_id :
            return True
        return False
    except Division.DoesNotExist :
        profile_div = None
    if profile_div==None:
        return False

def is_profile_in_your_equipe(request,pk):
    equipe_id = Equipe.objects.get(chef_equipe=request.user.id).id
    try:
        profile_equipe = Equipe.objects.get(researcher=pk).id
        if profile_equipe == equipe_id:
            return True
        return False
    except Equipe.DoesNotExist :
        profile_equipe = None
    try:
        profile_equipe=Equipe.objects.get(chef_equipe=pk).id
        if profile_equipe == equipe_id :
            return True
        return False
    except Equipe.DoesNotExist :
        profile_equipe = None
    if profile_equipe==None:
        return False