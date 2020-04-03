from django import forms
from .models import Cats

class CatAddForm(forms.ModelForm):
	class Meta:
		model = Cats
		fields = ['name', 'sex', 'age', 'breed', 'hair']

		labels = {
			'name': 'Имя',
			'sex': 'Пол',
			'age': 'Возраст',
			'breed': 'Порода',
			'hair': 'Волосатость',
		}

class CatUpdateForm(forms.ModelForm):
	class Meta:
		model = Cats
		fields = ['name', 'sex', 'age', 'breed', 'hair']

		labels = {
			'name': 'Имя',
			'sex': 'Пол',
			'age': 'Возраст',
			'breed': 'Порода',
			'hair': 'Волосатость',
		}
