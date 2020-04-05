from django.contrib import admin
from .models import Comments, Likes

admin.site.register(Likes)
admin.site.register(Comments)
