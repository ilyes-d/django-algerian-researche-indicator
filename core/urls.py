from django.contrib import admin
from django.urls import path, include 
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),          
    path("", include("apps.authentication.urls")), # Auth routes - login / register
    path('', include("apps.home.routes")),
    path("", include("apps.home.urls"))
]
urlpatterns += static(settings.MEDIA_URL,  document_root=settings.MEDIA_ROOT)
urlpatterns += staticfiles_urlpatterns()