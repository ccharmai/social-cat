from django.urls import path
from . import views

app_name = 'api'

urlpatterns = [
	path('cats/', views.CatsListView.as_view(), name='cats'),
	path('user/<pk>/', views.UserDetailView.as_view(), name='user'),
]
