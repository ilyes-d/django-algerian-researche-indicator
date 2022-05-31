from django.urls import path, include
from apps.home.views import _views, chef_div , chef_eta ,chef_equipe

urlpatterns = [

    path('', _views.index, name='home'),
         
    path('etablisement/' ,include([
        path('dashboard/' , chef_eta.dash_etablisemnt  , name='dashboard_etablisement'),
     ])),
     path('division/' ,include([
        path('dashboard/' , chef_div.dash_division  , name='dashboard_division'),
     ])),
     path('equipe/' ,include([
        path('dashboard/' , chef_equipe.dash_equipe  , name='dashboard_equipe'),
     ])),
    # re_path(r'^.*\.*', _views.pages, name='pages'),
    path('settings/', _views.settings , name= "settings"),
    path('try/' , _views.trying, name='try')
]
