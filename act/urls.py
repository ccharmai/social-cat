from django.urls import path
from . import views

app_name = 'act'

urlpatterns = [
	path('del/comm/<int:id>', views.CommentDeleteView, name='com_del'),
]