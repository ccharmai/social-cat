from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('crud.urls', namespace='crud')),
    path('auth/', include('django.contrib.auth.urls')),
    path('auth/', include('log.urls', namespace='log')),
    path('act/', include('act.urls', namespace='act')),
]
