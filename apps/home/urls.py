from django.urls import path, re_path, include
from apps.home.views import _views , chef_eta
urlpatterns = [

    path('', _views.index, name='home'),
    path('etablisement/' ,include([
        path('dashboard/' ,chef_eta.dash_etablisemnt  , name='dashboard_etablisement'),
     ])),
         
    # re_path(r'^.*\.*', _views.pages, name='pages'),
    path('settings/', _views.settings , name= "settings"),
    path('try/' , _views.trying, name='try')
]