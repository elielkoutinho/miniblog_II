from django.db import models

# Para deixar cada assunto e entrada com seus respectivos usuários 
from django.contrib.auth.models import User


class Topic(models.Model):
	text = models.CharField(max_length=200, verbose_name='assunto')
	date_added = models.DateTimeField(auto_now_add=True, verbose_name='Data')
	owner = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='autor')

	class Meta:
		verbose_name_plural = 'tópicos'

	def __str__(self):
		return self.text
		

class Entry(models.Model):
	topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
	text = models.TextField()
	date_added = models.DateTimeField(auto_now_add=True)

	class Meta:
		verbose_name_plural = 'entradas'

	def __str__(self):
		return self.text[:50] + "..."
