from django.urls import path, include
from apps.home.views import _views , chef_eta , organization
urlpatterns = [
        path('organisation/' ,include([
        path('dashboard/' , organization.dashboard, name="organization-dashboard"),
        path('etablisements/', organization.etablisements , name="organization-etablisements"),
    ])),    
]
