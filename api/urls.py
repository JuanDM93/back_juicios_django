from django.urls import path
from django.contrib import admin
from django.conf.urls import include, url


urlpatterns = [
    
    # DB access
    path('admin/', admin.site.urls),    
    
    # APIs access
    path('accounts/', include('api.accounts.urls')),
    path('locals/', include('api.locals.urls')),
    path('federals/', include('api.federals.urls')),

    # REST AUTH
    path('api-auth/', include('rest_framework.urls')),
]