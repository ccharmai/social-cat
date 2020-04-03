from django.db import models
from django.urls import reverse
from django.core.validators import MinValueValidator, MaxValueValidator
from django.contrib.auth.models import User

HAIR_CHOICES = [
	['0', 'Лысый'],
	['1', 'Слегка волосатый'],
	['2', 'Нормально волосатый'],
	['3', 'Сильно волосатый'],
	['4', 'Одни волосы'],
]

SEX_CHOICES = [
	['m', 'Мужской'],
	['z', 'Женский'],
]

class Cats(models.Model):
	owner = models.ForeignKey(User, related_name='cat', on_delete=models.CASCADE)

	name = models.CharField(max_length=50)
	sex = models.CharField(max_length=1, choices=SEX_CHOICES, default='m')
	age = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(20)])
	breed = models.CharField(max_length=50)
	hair = models.CharField(max_length=1, choices=HAIR_CHOICES, default='2')

	class Meta:
		verbose_name = 'Кот'
		verbose_name_plural = 'Коты'

	def __str__(self):
		return f'Кот {self.name}, хозяин - {self.owner}'

	def get_absolute_url(self):
		return reverse('crud:cat', args=[self.id])

