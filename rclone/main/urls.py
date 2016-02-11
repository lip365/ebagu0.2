from django.conf.urls import url
from main.views import *

from main import views
from django.conf.urls import include, url

from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required as auth


urlpatterns = [
		url(r'^$', 'main.views.index', name='index'),
		url(r'^post/(?P<slug>[-\w]+)/vote/$', 'main.views.vote', name='vote'),
		#url(r'^add_post/', views.add_post, name='add_post'),

		url(r'^add_post/$', PostCreateView.as_view(), name='post-add'),
		url(r'^category/(?P<category_name_url>\w+)/$', views.category, name='category'),
		
		url(r'^add_category/', views.add_category, name='add_category'),
		# url(r'^(?P<slug>[\w|\-]+)/$', views.post, name='post'),
		url(r'^search/$', views.search_titles),
		url(r'^post/(?P<slug>[\w|\-]+)/$', views.post, name='post'),
		
   	

	    url(r'^follow/(?P<category_name_url>\w+)/$', 'main.views.follow', name='follow'),
	    url(r'^unfollow/(?P<category_name_url>\w+)/$', 'main.views.unfollow', name='unfollow'),

		url(r'^post/edit/(?P<slug>[\w|\-]+)/$', PostUpdateView.as_view(), name='post-edit'),
		url(r'^post/delete/(?P<slug>[\w|\-]+)/$', PostDeleteView.as_view(), name='post-delete'),
		]

		