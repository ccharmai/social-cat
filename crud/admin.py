from django.contrib import admin
from .models import Cats

class AdminCat(admin.ModelAdmin):
	list_display = ['id', 'name']

admin.site.register(Cats, AdminCat)
