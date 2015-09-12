import datetime

from django.db import models
from django.utils import timezone

# Create your models here.
class Question(models.Model):
	question_text = models.CharField(max_length=200)
	questioner = models.CharField(max_length=100)
	pub_date = models.DateTimeField('date published')

	def published_recently(self):
		return self.pub_date >= timezone.now() - datetime.timedelta(hours=2)

	def __str__(self):
		return self.question_text


class Choice(models.Model):
	question = models.ForeignKey(Question)
	choice_text = models.CharField(max_length=200)
	choice_date = models.DateTimeField('date answered')
	votes = models.IntegerField(default=0)

	def __str__(self):
		return self.choice_text