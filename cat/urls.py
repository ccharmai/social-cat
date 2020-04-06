from django.contrib import admin
from django.urls import path, include
from django.shortcuts import redirect
from act.views import LogRedirect

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('crud.urls', namespace='crud')),
    path('auth/', include('django.contrib.auth.urls')),
    path('auth/', include('log.urls', namespace='log')),
    path('act/', include('act.urls', namespace='act')),

    path('api/', include('api.urls', namespace='api')),

    path('accounts/login/', LogRedirect),
]
