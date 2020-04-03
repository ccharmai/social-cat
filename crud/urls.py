from django.urls import path
from . import views

app_name = 'crud'

urlpatterns = [
	path('', views.HomeView, name='home'),
	path('<int:id>/', views.CatView, name='cat'),
	path('add/', views.AddView, name='add_cat'),
	path('del/<int:id>/', views.DelView, name='del_cat'),
	path('update/<int:id>', views.UpdateView, name='update_cat'),
	path('lk/', views.LKView, name='lk'),
]