
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify
from uuslug import uuslug
from froala_editor.fields import FroalaField


# Create your models here.
class Category(models.Model): 
	name = models.CharField(max_length=128, unique=True)
	likes = models.IntegerField(default=0)
	slug = models.SlugField(unique=True)
	
	def save(self, *args, **kwargs):
		self.slug = slugify(self.name)
		super(Category, self).save(*args, **kwargs)
        
	def __unicode__(self): 
		return self.name

class Post(models.Model):
	category = models.ForeignKey(Category)
	created_at = models.DateTimeField(auto_now_add = True)
	title = models.CharField(max_length = 100)
	content = FroalaField()
	url = models.URLField(max_length=250, blank=True)
	ups = models.IntegerField(default=0)
	down = models.IntegerField(default=0)
	score = models.IntegerField(default=0)
	views = models.IntegerField(default=0)
	image = models.ImageField(upload_to="images",blank=True, null=True)
	slug = models.CharField(max_length=100, unique=True)
    

  	def save(self, *args, **kwargs):
  		self.slug = uuslug(self.title, instance=self, max_length=100)
  		super(Post, self).save(*args, **kwargs)
	def __unicode__(self):
		return self.title    	


class UserProfile(models.Model):
	picture = models.ImageField(upload_to='profile_images', blank=True)
	website = models.URLField(blank=True)
	user = models.OneToOneField(User)

	def __unicode__(self):
		return self.user.username