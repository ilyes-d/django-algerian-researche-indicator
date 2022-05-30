from django.urls import path, include
from apps.home.views import _views , chef_eta , organization
urlpatterns = [
        path('organization/' ,include([
        path('dashboard/' , organization.dashboard, name="organizations-dashboard"),
        path('etablisements/', organization.etablisements , name="organizations-etablisements"),
    ])),    
]
