from django.db import models
from crud.models import Cats
from django.contrib.auth.models import User

class Comments(models.Model):
	cat = models.ForeignKey(Cats, related_name='comment', on_delete=models.CASCADE)
	commentator = models.ForeignKey(User, related_name='commentator', on_delete=models.CASCADE)

	body = models.CharField(max_length=150)

	created = models.DateTimeField(auto_now_add=True)

	deleted = models.BooleanField(default=False)

	class Meta:
		ordering = ('created',)
		verbose_name = 'Комментарий'
		verbose_name_plural = 'Комментарии'

	def __str__(self):
		return f'Комментарий {self.commentator} к коту {self.cat.name} - {self.body}'

class Likes(models.Model):
	cat = models.ForeignKey(Cats, related_name='cat', on_delete=models.CASCADE)
	user = models.ForeignKey(User, related_name='user', on_delete=models.CASCADE)

	class Meta:
		verbose_name = 'Лайк'
		verbose_name_plural = 'Лайки'

	def __str__(self):
		return f'{self.user.username} лайкнул {self.cat.name}а'

