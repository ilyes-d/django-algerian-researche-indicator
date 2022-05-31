from django.urls import path, include
from apps.home.views import _views, chef_div , chef_eta ,chef_equipe

urlpatterns = [

    path('', _views.index, name='home'),
         
    path('etablisement/' ,include([
        path('dashboard/' , chef_eta.dash_etablisemnt  , name='dashboard_etablisement'),
        path('division/liste/' , chef_eta.dash_etablisemnt  , name='division_etablisement'),
        path('equipe/liste/' , chef_eta.dash_etablisemnt  , name='equipe_etablisement'),
        path('chercheur/card/' , chef_eta.dash_etablisemnt  , name='chercheur_card_etablisement'),
        path('chercheur/list/' , chef_eta.dash_etablisemnt  , name='dashboard_etablisement'),
     ])),
     path('division/' ,include([
        path('dashboard/' , chef_div.dash_division  , name='dashboard_division'),
        path('equipe/liste/' ,   chef_div.dash_etablisemnt  , name='equipe_division'),
        path('chercheur/card/' , chef_div.dash_etablisemnt  , name='chercheur_card_division'),
        path('chercheur/list/' , chef_div.dash_etablisemnt  , name='chercheur_list_division'),
     ])),
     path('equipe/' ,include([
        path('dashboard/' , chef_equipe.dash_equipe  , name='dashboard_equipe'),
     ])),
    # re_path(r'^.*\.*', _views.pages, name='pages'),
    path('settings/', _views.settings , name= "settings"),
    path('try/' , _views.trying, name='try')
]
