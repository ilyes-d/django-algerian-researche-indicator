from django.urls import path, include
from apps.home.views import _views , chef_eta , chef_equipe,filters,org
urlpatterns = [
    # path('equipe/', include([
    #     path('dashboard/', chef_equipe.equipe_dashboard, name="equipe-dashboard"),
    #     path('members/', chef_equipe.equipe_members , name="equipe-memnbers"),
    # ])),
    
    #  those only for the superuser MESRS
    path('organisation/' ,include([
        path('dashboard/' , org.org_dashboard, name="org-dashboard"),
        path('etablisement/dashboard/', org.org_etas_dash , name="org-etas-dash"),
        path('etablisements/liste/', org.org_etas_liste, name="org-etas-liste"),
        path('divisions/dashboard/', org.org_divs_dash, name ="org-divs-dash"),
        path('division/liste/', org.org_divs_liste, name="org-divs-liste"),
        path('equipes/dashboard/', org.org_equipes_dash , name = "org-equipes-dash"),
        path('equipe/liste/', org.org_equipes_liste, name="org-equipes-liste")
    ])),
    
    path('try/', filters.etablisement_list)

    # path('member/', include([
    #     path('dashboard/', )
    # ]))    
]
