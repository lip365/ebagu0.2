# -*- coding: utf-8 -*-
from django.conf.urls import url
from main.views import *
from accounts.forms import SignupFormExtra

from main import views

from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required as auth

urlpatterns = [
	url(r'^$', 'main.views.index', name='index'),
	url(r'^post/(?P<slug>[-\w]+)/vote/$', 'main.views.vote', name='vote'),
	#url(r'^add_post/', views.add_post, name='add_post'),
	url(r'^add_post/$', PostCreateView.as_view(), name='post-add'),
	url(r'^category/(?P<category_name_slug>[\w\-]+)/$', views.category, name='category'),
	url(r'^(?P<slug>[\w|\-]+)/edit/$', PostUpdateView.as_view(), name='post-edit'),
	url(r'^(?P<slug>[\w|\-]+)/delete/$', PostDeleteView.as_view(), name='post-delete'),
	url(r'^add_category/', views.add_category, name='add_category'),
	url(r'^(?P<slug>[\w|\-]+)/$', views.post, name='post'),
	url(r'^search/$', 'main.views.search_titles'),
	url(r'^accounts/signup/$','userena.views.signup',{'signup_form': SignupFormExtra}),
	]