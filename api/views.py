from rest_framework import generics
from crud.models import Cats
from django.contrib.auth.models import User
from .serializers import CatsSerializer, UserSerializer


class CatsListView(generics.ListAPIView):
	queryset = Cats.objects.all()
	serializer_class = CatsSerializer

class UserDetailView(generics.RetrieveAPIView):
	queryset = User.objects.all()
	serializer_class = UserSerializer
