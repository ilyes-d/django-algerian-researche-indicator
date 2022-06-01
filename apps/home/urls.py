from django.urls import path, include
from apps.home.views import _views, chef_div , chef_eta ,chef_equipe

urlpatterns = [

    path('', _views.index, name='home'),
         
    path('etablisement/' ,include([
        path('dashboard/' , chef_eta.dash_etablisemnt  , name='dashboard-etablisement'),
        path('divisions/liste/' , chef_eta.dash_etablisemnt  , name='divisions-of-etablisement'),
        path('equipes/liste/' , chef_eta.equipes_of_etablisement  , name='equipes-of-etablisement'),
      #   path('equipe/<int:pk>/chercheurs' , chef_eta.dash_etablisemnt  , name='cherch-of-etablisement'),
        path('chercheurs/card/' , chef_eta.dash_etablisemnt  , name='chercheurs_card_etablisement'),
        path('chercheurs/liste/' , chef_eta.dash_etablisemnt  , name='chercheurs_liste_etablisement'),
     ])),
     path('division/' ,include([
        path('dashboard/' , chef_div.dash_division  , name='dashboard_division'),
        path('equipe/liste/' ,   chef_div.dash_division  , name='equipe_division'),
        path('chercheur/card/' , chef_div.dash_division  , name='chercheur_card_division'),
        path('chercheur/list/' , chef_div.dash_division  , name='chercheur_list_division'),
     ])),
    path('try/' , _views.trying, name='try')
]
