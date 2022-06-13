from django.urls import path, include
from apps.home.views import chef_eta , div, equipe,filters,org,users
from .views.users import *



urlpatterns = [
    
    path('', users.index, name='index'),
    
    #  those only for the superuser MESRS
    path('refrech-database/', org.refrech_database , name='refrech'),
    path('organisation/' ,include([
        path('carte/' , org.org_carte, name="org-carte"),
        path('dashboard/' , org.org_dashboard, name="org-dashboard"),
        path('etablisements/liste/', org.org_etas_liste, name="org-etas-liste"),
        path('division/liste/', org.org_divs_liste, name="org-divs-liste"),
        path('equipe/liste/', org.org_equipes_liste, name="org-equipes-liste"),
        path('chercheurs/members/liste/', org.org_members_liste, name="org-members-liste"),
        path('chercheurs/chef-eta/liste/', org.org_chef_eta_liste, name="org-chefeta-liste"),
        path('chercheurs/chef-div/liste/', org.org_chef_div_liste, name="org-chefdiv-liste"),
        path('chercheurs/chef-equ/liste/', org.org_chef_equ_liste, name="org-chefequ-liste"),
        
        
        path('etablisement/dashboard/', org.org_etas_dash , name="org-etas-dash"),
        path('divisions/dashboard/', org.org_divs_dash, name ="org-divs-dash"),
        path('equipes/dashboard/', org.org_equipes_dash , name = "org-equipes-dash"),
    ])),
    
    path('try/', filters.etablisement_list),
    path('filter/', div.search, name='search'),
    path('members/',users.member , name='members'),
    
    path('eta=<int:pk>/',chef_eta.dash_etablisemnts,name='eta-dash-pk'),
    
    



    path('etablisement=<int:eta_id>/' ,include([
        
        # path('divisions/dash/' , chef_eta.eta_divs_dash  , name='divisions-of-etablisement'),
        # path('equipes/dashboard/',chef_eta.eta_equipes_dash  , name='eta-equipes-dash'),
        # path('chercheurs/card/' , chef_eta.eta_chers_dash  , name='eta-chers-liste'),
        
        # path('chercheurs/card/' , chef_eta.Liste_cher_Eta_aff_list  , name='chercheur-list-'),
        
        path('dashboard/' , chef_eta.eta_dash  , name='eta-dash'),
     ])),
    path('divisions/liste/' , chef_eta.Liste_division_Eta_aff_list  , name='eta-divs-liste'),
    path('equipes/liste/',chef_eta.eta_equipes_liste  ,    name='eta-equipes-liste'),
    path('members/' , chef_eta.Liste_cher_Eta_aff_list  , name='eta-members-liste'),
    path('chef-divs/' , chef_eta.Liste_cher_Eta_aff_list  , name='eta-chefdivs-liste'),
    path('chef-equipes/' , chef_eta.eta_chers_liste, name='eta-chefequ-liste'),
    
    # chef division
    path('division/' ,include([   
        path('dashboard/' , div.div_dash  , name='div-dash'),
        path('equipes/liste/' ,div.div_equipe_liste  , name='div-equipes-liste'),
        path('members/',div.div_chers_liste_card , name='div-members-liste'),
        path('chef-equipe/',div.div_chers_liste, name='div-chefequ-liste'),
        
    ])),
    
    #  chef equipe
    path('equipe/' ,include([    
        path('dashboard/' , equipe.equipe_dash , name='equipe-dash'),
        path('members/' , equipe.equipe_chers_dash, name='equipe-chers-liste'),
        
     ])),    
    
    
    
    path('profile/user=<int:pk>', researcher_profile , name='researcher_profile')
]



# for handling 404 errors
def handler404(request, exception=None):
    return render(request,'404.html')
    
handler404 = handler404