import datetime

from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class ActionItem(models.Model):
	OPEN_ACTION = 1
	COMPLETED_ACTION = 2
	TABLED_ACTION = 3
	STATUS_CHOICES = (
		(OPEN_ACTION, 'Open'),
		(COMPLETED_ACTION, 'Complete'),
		(TABLED_ACTION, 'Tabled'),
	)
	
	title = models.CharField(max_length=250)
	slug = models.SlugField(unique=True)
	description = models.TextField()
	owner = models.ForeignKey(User, blank=True)
	requester = models.CharField(max_length=250, blank=True)
	due_date = models.DateTimeField(default=datetime.datetime.now, blank=True)
	status = models.IntegerField(choices=STATUS_CHOICES, default=OPEN_ACTION)
	red_tape_ID = models.CharField(max_length=250, blank=True)
	
	class Meta:
		ordering = ['slug']
		
	def get_absolute_url(self):
		pass
	
	
	def __unicode__(self):
		return self.slug
		
class Tweet(models.Model):
	owner = models.ForeignKey(User)
	tweet = models.TextField(max_length=500)
	id = models.AutoField(primary_key=True)
	creation_date = models.DateTimeField(default=datetime.datetime.now)

	class Meta:
		ordering = ['creation_date']
		
	def get_absolute_url(self):
		pass
	
	
	def __unicode__(self):
		return self.tweet	
	
