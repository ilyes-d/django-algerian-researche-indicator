from django.urls import path, include
from apps.home.views import _views, chef_div , chef_eta ,chef_equipe
from django.shortcuts import render 
from .views.users import *
def handler404(request, exception=None):
    return render(request,'404.html')
    
handler404 = handler404

urlpatterns = [

    path('', _views.index, name='index'),
    #  chef etablisement
    path('etablisement/' ,include([
        path('dashboard/' , chef_eta.eta_dash  , name='eta-dash'),
        # 
        path('divisions/dash/' , chef_eta.eta_divs_dash  , name='divisions-of-etablisement'),
        path('divisions/liste/' , chef_eta.Liste_division_Eta_aff_list  , name='divisions-of-etablisement'),
        # 
        path('equipes/dashboard/',chef_eta.eta_equipes_dash  , name='eta-equipes-dash'),
        path('equipes/liste/',chef_eta.eta_equipes_liste  ,    name='eta-equipes-liste'),
        # 
        path('chercheurs/card/' , chef_eta.eta_chers_dash  , name='eta-chers-liste'),
        path('chercheurs/card/' , chef_eta.Liste_cher_Eta_aff_list  , name='chercheur-list-'),
        path('chercheurs/liste/' , chef_eta.eta_chers_liste, name='eta-chers-liste'),
     ])),
    
    # chef division
     path('division/' ,include([
        path('dashboard/' , chef_div.div_dash  , name='div-dash'),
        path('equipes/dashboard/' ,chef_div.div_equipe_dashboard,name='div-equipes-dash'),
        path('equipes/liste/' ,chef_div.div_equipe_liste  , name='div-equipes-liste'),
        path('chercheurs/dashboard/',chef_div.div_chers_dash , name='div-chers-dash'),
        path('chercheurs/card/',chef_div.div_chers_liste_card , name='div-chers-liste-card'),
        path('chercheurs/liste/',chef_div.div_chers_liste, name='div-chers-liste'),
     ])),
     
     
    #  chef equipe
    path('equipe/' ,include([
        path('dashboard/' , chef_equipe.equipe_dash , name='equipe-dash'),
        path('chercheurs/dash/' , chef_equipe.equipe_chers_dash, name='equipe-chers-dash'),
        path('chercheurs/liste/' , chef_equipe.equipe_chers_liste  , name='equipe-chers-liste'),
     ])),    
    
    # All users  
    path('profile/user=<str:pk>', researcher_profile , name='researcher_profile')
]
