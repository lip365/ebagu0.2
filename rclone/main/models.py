	# -*- coding: utf-8 -*-
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from uuslug import uuslug
from urlparse import urlparse
from django.conf import settings

from main.util.ranking import hot

from django.db.models.signals import post_save
from froala_editor.fields import FroalaField
from redactor.fields import RedactorField
from embed_video.fields import EmbedVideoField
from ckeditor_uploader.fields import RichTextUploadingField



from mptt.models import MPTTModel, TreeForeignKey
from main.util.model_utils import ContentTypeAware, MttpContentTypeAware




from django.db.models.signals import post_save
from actstream import action


# Create your models here.
class Category(models.Model): 
	
	name = models.CharField(max_length=128, unique=True)
	description = models.TextField(verbose_name=('커뮤니티 설명'))
	author = models.ForeignKey(settings.AUTH_USER_MODEL)
	

	def __unicode__(self): 
		return self.name

	def get_absolute_url(self):
		return "/category/%s/" %self.name

def my_handler(sender, instance, created, **kwargs):
	action.send(instance.author, verb='following', target=Category)
post_save.connect(my_handler, sender=Category)


class Post(models.Model):
	category = models.ForeignKey(Category, verbose_name=('커뮤니티'))
	pub_date = models.DateTimeField(auto_now_add = True)
	url = models.URLField(max_length=250, blank=True, null=True)
	video = EmbedVideoField(verbose_name='동영상링크',help_text="Youtube주소만 입력해주세요", blank=True, null=True)	

	title = models.CharField(max_length = 100)
	moderator = models.ForeignKey(User)
	views = models.IntegerField(default=0)
	slug = models.CharField(max_length=100, unique=True)
	objects = models.Manager()            # default manager
	content = RichTextUploadingField(config_name='default')
	rank_score = models.FloatField(default= 1)
	image = models.ImageField(upload_to='images',blank=True, null=True)
	thumbnail = models.ImageField(upload_to='images', blank=True, null=True)
	comment_count = models.IntegerField(default=0)

		
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

class Comment(MttpContentTypeAware):
	post = models.ForeignKey(Post)
	writer = models.ForeignKey(User)
	parent = TreeForeignKey('self', related_name='children',
							null=True, blank=True, db_index=True)
	timestamp = models.DateTimeField(default=timezone.now)
	ups = models.IntegerField(default=0)
	downs = models.IntegerField(default=0)
	score = models.IntegerField(default=0)
	raw_comment = models.TextField(blank=True)
	html_comment = models.TextField(blank=True)
	
	class MPTTMeta:
			order_insertion_by = ['-score']

			@classmethod
			def create(cls, author, raw_comment, parent):
				"""
				Create a new comment instance. If the parent is submisison
				update comment_count field and save it.
				If parent is comment post it as child comment
				:param author: RedditUser instance
				:type author: RedditUser
				:param raw_comment: Raw comment text
				:type raw_comment: str
				:param parent: Comment or Submission that this comment is child of
				:type parent: Comment | Submission
				:return: New Comment instance
				:rtype: Comment
				"""

				html_comment = mistune.markdown(raw_comment)
				# todo: any exceptions possible?
				comment = cls(author=author,
							  author_name=author.user.username,
							  raw_comment=raw_comment,
							  html_comment=html_comment)

				if isinstance(parent, Submission):
					submission = parent
					comment.submission = submission
				elif isinstance(parent, Comment):
					submission = parent.submission
					comment.submission = submission
					comment.parent = parent
				else:
					return
				submission.comment_count += 1
				submission.save()

				return comment

			def __unicode__(self):
				return "<Comment:{}>".format(self.id)


