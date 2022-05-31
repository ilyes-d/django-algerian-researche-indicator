from django.urls import path, include
from apps.home.views import _views , chef_eta , organization, chef_equipe
urlpatterns = [
    # path('equipe/', include([
    #     path('dashboard/', chef_equipe.equipe_dashboard, name="equipe-dashboard"),
    #     path('members/', chef_equipe.equipe_members , name="equipe-memnbers"),
    # ])),
    path('organisation/' ,include([
        path('dashboard/' , organization.org_dashboard, name="org-dashboard"),
        path('etablisements/', organization.org_etablisements , name="org-etablisements"),
        path('etablisement/divisions/', organization.divisions_of_etablisement , name="divisions-of-etablisement"),
        path('etablisement/equipes/', organization.divisions_of_etablisement , name="divisions-of-etablisement"),
        # path('etablisement/<int:pk>/divisions/', organization.divisions_of_etablisement , name="divisions-of-etablisement"),
        path('divisions/', organization.org_divisions , name ="org-divisions"),
        path('division/<int:pk>/equipes/', organization.equipes_of_division, name="equipes-of-division"),
        path('equipes/', organization.org_equipes , name = "org-equipes"),
        path('equipe/<int:pk>/members/', organization.members_of_equipe, name="members-of-equipe")
    ])),
    # path('member/', include([
    #     path('dashboard/', )
    # ]))    
]
