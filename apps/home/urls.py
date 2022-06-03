from django.urls import path, include
from apps.home.views import _views, chef_div , chef_eta ,chef_equipe

urlpatterns = [

    path('', _views.index, name='home'),
         
    path('etablisement/' ,include([

        path('dashboard/' , chef_eta.dash_etablisemnt  , name='dashboard_etablisement'),
        path('divisions/liste/' , chef_eta.Liste_division_Eta_aff_list  , name='divisions-of-etablisement'),
        path('equipes/liste/' , chef_eta.Liste_equipe_Eta_aff_list  , name='equipe-of-etablisement'),
        path('chercheurs/card/' , chef_eta.Liste_cher_Eta_aff_list  , name='chercheur_list_etablisement'),
        path('chercheurs/liste/' , chef_eta.Liste_cher_Eta_aff  , name='chercheurs_card_etablisement'),
     ])),
     path('division/' ,include([
        path('dashboard/' , chef_div.dash_division  , name='dashboard_division'),
        path('equipe/liste/' ,   chef_div.Liste_equipe_Div_aff_list  , name='equipe_division'),
        path('chercheur/card/' , chef_div.Liste_cher_Div_aff_card  , name='chercheur_card_division'),
        path('chercheur/list/' , chef_div.Liste_cher_Div_aff_list  , name='chercheur_list_division'),
     ])),
    path('equipe/' ,include([
        path('dashboard/' , chef_equipe.dash_equipe , name='dashboard_equipe'),
        path('chercheur/list/' , chef_equipe.Liste_cher_Equipe_aff_list  , name='chercheur_list_equipe'),
     ])),
]
