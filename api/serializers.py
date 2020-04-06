from rest_framework import serializers
from crud.models import Cats
from django.contrib.auth.models import User

class CatsSerializer(serializers.ModelSerializer):
	class Meta:
		model = Cats
		fields = ['id', 'owner', 'name', 'sex', 'age', 'breed', 'hair']

class UserSerializer(serializers.ModelSerializer):
	class Meta:
		model = User
		fields = ['id', 'username']
