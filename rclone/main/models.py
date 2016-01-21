# -*- coding: utf-8 -*-
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from uuslug import uuslug
from urlparse import urlparse
from django.conf import settings

from froala_editor.fields import FroalaField
from main.util.ranking import hot

from django.db.models.signals import post_save
from actstream import action

# Create your models here.
class Category(models.Model): 
	name = models.CharField(max_length=128, unique=True)
	description = models.CharField(max_length=200, unique=True)
	image = models.FileField(upload_to='images',blank=True, null=True)
	author = models.ForeignKey(settings.AUTH_USER_MODEL)
	
	def __unicode__(self): 
		return self.name

	def get_absolute_url(self):
		return "/category/%s/" %self.name

def new_category(sender, instance, created, **kwargs):
    action.send(instance.user, verb='posted', target=instance, mood='sleepy')
		
post_save.connect(new_category, sender=Category)


class Post(models.Model):
	category = models.ForeignKey(Category)
	pub_date = models.DateTimeField(auto_now_add = True)
	title = models.CharField(max_length = 100)
	url = models.URLField(max_length=250, blank=True, null=True)
	moderator = models.ForeignKey(User)
	views = models.IntegerField(default=0)
	slug = models.CharField(max_length=100, unique=True)
	objects = models.Manager()            # default manager
	
	content = FroalaField()
	rank_score = models.FloatField(default= 1)
	image = models.ImageField(upload_to='images',blank=True, null=True)

	@property
	def domain(self):
		long_url = urlparse(self.url).netloc if self.url else "be kind to one another"
		return long_url.split('.', 1)[1] if long_url.split('.', 1)[0] == 'www' else long_url
	def save(self, *args, **kwargs):
		self.slug = uuslug(self.title, instance=self, max_length=100)
		super(Post, self).save(*args, **kwargs)
	def __unicode__(self):
		return self.title 
 

	# for redirecting URL so slug is always shown
	def get_absolute_url(self):
		return '/%s/%s' % (self.id, self.slug)


	def get_vote_count(self):
		"""This function is intended to return count of voted on thread.
		:return: The sum of vote, upvote - devote
		"""
		vote_count = self.vote_set.filter(is_up=True).count() - self.vote_set.filter(is_up=False).count()
		if vote_count >= 0:
			return "+ " + str(vote_count)
		else:
			return "- " + str(abs(vote_count))

	def get_score(self):
		""" This function is intended to return score calculated by hot ranking algorithm from reddit.
		Check out URL containing detail of hot ranking algorithm in news.util.ranking.py
		:return: The score calculated by hot ranking algorithm
		"""
		upvote_count = self.vote_set.filter(is_up=True).count()
		devote_count = self.vote_set.filter(is_up=False).count()
		return hot(upvote_count, devote_count, self.pub_date.replace(tzinfo=None))




class Vote(models.Model):
	post = models.ForeignKey(Post)
	user = models.ForeignKey(User)
	is_up = models.BooleanField("good", default=True)

	def __unicode__(self):
		result = self.user.username + " vote to post id " + str(self.post.id)
		if self.is_up:
			return result + " with +1"
		else:
			return result + " with -1"
			
