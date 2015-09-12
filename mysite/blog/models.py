from django.db import models
from django.utils import timezone

class Post(models.Model): 
	# models.Model means that the Post is a Django Model
	# so Django knows that it should be saved in the database
	author = models.ForeignKey('auth.user')  
	# models.ForeignKey is a link to another model
	title = models.CharField(max_length=200)
	text = models.TextField()
	create_date = models.DateTimeField(default=timezone.now)
	pub_date = models.DateTimeField(blank=True, null=True)

	def publish(self):
		self.pub_date = timezone.now()
		self.save()

	def __str__(self):
		return self.title
