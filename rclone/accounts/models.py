# -*- coding: utf-8 -*-
from django.db import models

# Create your models here.
from django.contrib.auth.models import User
from django.utils.translation import ugettext as _
from userena.models import UserenaBaseProfile

class MyProfile(UserenaBaseProfile):
    user = models.OneToOneField(User, unique=True, verbose_name=_('user'), related_name='my_profile')
    location = models.CharField(max_length=255, blank=True)
    website = models.URLField(max_length=255, blank=True)
    twitter = models.CharField(max_length=255, blank=True)