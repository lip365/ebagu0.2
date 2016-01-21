from django.conf.urls import url
from main.views import *

from main import views

from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required as auth


urlpatterns = [
		url(r'^$', 'main.views.index', name='index'),
		url(r'^post/(?P<slug>[-\w]+)/vote/$', 'main.views.vote', name='vote'),
		#url(r'^add_post/', views.add_post, name='add_post'),
		url(r'^add_post/$', PostCreateView.as_view(), name='post-add'),
		url(r'^category/(?P<category_name_url>\w+)/$', views.category, name='category'),
		url(r'^unfollow/(?P<category_name_url>\w+)/', 'main.views.unfollow_user', name='unfollow'),
		   url(r'^follow/(?P<category>\w+)/', 'main.views.follow_user', name='follow'),

		url(r'^add_category/', views.add_category, name='add_category'),
		# url(r'^(?P<slug>[\w|\-]+)/$', views.post, name='post'),
		url(r'^search/$', views.search_titles),
		url(r'^post/(?P<slug>[\w|\-]+)/$', views.post, name='post'),

		url(r'^edit/(?P<slug>[\w|\-]+)/$', PostUpdateView.as_view(), name='post-edit'),
		url(r'^delete/(?P<slug>[\w|\-]+)/$', PostDeleteView.as_view(), name='post-delete'),
		]
