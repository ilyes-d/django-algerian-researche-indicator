from django.urls import path, include

from apps.home.views import div, equipe, eta,org,users
from .views.users import *
from apps.home.views import div, equipe, eta,org,users
from apps.home.views.crud import *
from core import settings
from .views.users import *
from django.conf.urls.static import static


urlpatterns = [
    
    path('', users.index, name='index'),
    path('refrech-database/', org.refrech_database , name='refrech'),
    path('organisation/' ,include([
        path('carte/' , org.org_carte, name="org-carte"),
        path('dashboard/' , org.org_dashboard, name="org-dashboard"),
        path('etablisements/liste/', org.org_etas_liste, name="org-etas-liste"),
        path('etablisements/add/', creat_Etablisment_views, name="org-etas-add"),
        path('etablisements/delete/<str:pk>', Delete_Etablisment_views, name="org-etas-delete"),
        
        path('division/liste/', org.org_divs_liste, name="org-divs-liste"),
        path('division/add/', creat_division_views, name="org-divs-add"),
        path('division/delete/<str:pk>',Delete_Division_views, name="org-divs-delete"),
        
        path('equipe/liste/', org.org_equipes_liste, name="org-equipes-liste"),
        path('equipe/add/', creat_equipe_views, name="org-equipes-add"),
        path('equipe/upadate/<str:pk>', update_equipe_views, name="org-equipes-update"),
        path('equipe/delete/<str:pk>',Delete_Equipe_views, name="org-equipes-delete"),
        
        path('chercheurs/members/liste/', org.org_members_liste, name="org-members-liste"),
        path('chercheurs/chef-eta/liste/', org.org_chef_eta_liste, name="org-chefeta-liste"),
        path('chercheurs/chef-div/liste/', org.org_chef_div_liste, name="org-chefdiv-liste"),
        path('chercheurs/chef-equ/liste/', org.org_chef_equ_liste, name="org-chefequ-liste"),
        
        path('etablisement=<int:eta_id>/dashboard/',eta.eta_dash  , name="org-etas-dash"),
        path('division=<int:div_id>/dashboard/',div.div_dash , name ="org-div-dash"),
        path('equipe=<int:equ_id>/dashboard/' , equipe.equipe_dash , name='org-equipe-dash'),
    ])),        
    path('eta=<int:pk>/',eta.dash_etablisemnts,name='eta-dash-pk'),

    path('etablisement=<int:eta_id>/' ,include([
        path('dashboard/' , eta.eta_dash  , name='eta-dash'),
        path('divisions/liste/' , eta.eta_divs_liste , name='eta-divs-liste'),
        
        # """
        path('divisions/dash/' , eta.eta_divs_dash  , name='divisions-of-etablisement'),
        path('equipes/dashboard/',eta.eta_equipes_dash  , name='eta-equipes-dash'),
        path('chercheurs/card/' , eta.eta_chers_dash  , name='eta-chers-liste'),
        
        path('chercheurs/card/' , eta.Liste_cher_Eta_aff_list  , name='chercheur-list-'),
        path('equipes/liste/',eta.eta_equipes_liste  ,    name='eta-equipes-liste'),
        path('members/' , eta.Liste_cher_Eta_aff_list  , name='eta-members-liste'),
        path('chef-divs/' , eta.Liste_cher_Eta_aff_list  , name='eta-chefdivs-liste'),
        path('chef-equipes/' , eta.eta_chers_liste, name='eta-chefequ-liste'),
        # """
     ])),
    
    
    path('division=<int:div_id>/' ,include([
        path('dashboard/' , div.div_dash  , name='div-dash'),
        path('equipes/liste/' ,div.div_equipe_liste  , name='div-equipes-liste'),
        path('members/',div.div_chers_liste_card , name='div-members-liste'),
        path('chef-equipe/',div.div_chers_liste, name='div-chefequ-liste'),
        
    ])),
    
    #  chef equipe
    path('equipe=<int:equ_id>/' ,include([
        path('dashboard/' , equipe.equipe_dash , name='equipe-dash'),
        path('members/' , equipe.equipe_chers_dash, name='equipe-chers-liste'),
     ])),    
    
    path('profile/user=<int:pk>', researcher_profile , name='researcher_profile'),

    path('ajax/divs-liste/', org.org_divs_liste_v2, name="div-ajax-liste"),
    path('ajax/load-etas',org.load_etas , name='eta-options'),
    path('ajax/load-divs',org.load_divs , name='div-options'),
    path('ajax/load-equipes',org.load_equipes , name='equipe-options'),
    path('ajax/eta-liste',org.wilaya_etas_liste , name='eta-liste'),
    path('ajax/members-liste',org.members_liste , name='members-ajax-liste'),
    # path('ajax/get_divs',eta.get_div_liste , name='divs-liste'),
    path('profile/update/', researcher_profile_update , name='researcher_profile_update'),
    
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# for handling 404 errors
def handler404(request, exception=None):
    return render(request,'404.html')
    
handler404 = handler404

