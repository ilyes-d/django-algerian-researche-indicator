from django.contrib import admin
from django.urls import path, include 


urlpatterns = [
    path('admin/', admin.site.urls),          
    path("", include("apps.authentication.urls")), # Auth routes - login / register
    path('', include("apps.home.routes")),
    path("", include("apps.home.urls"))
]
