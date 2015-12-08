from django.conf.urls import url
from main import views
from django.core.urlresolvers import reverse
from views import *

urlpatterns = [
	url(r'^$', views.index, name='index'),

	#url(r'^add_post/', views.add_post, name='add_post'),
	url(r'^add_post/$', PostCreateView.as_view(), name='post-add'),

    url(r'^(?P<slug>[\w|\-]+)/edit/$', PostUpdateView.as_view(), name='post-edit'),
    url(r'^(?P<slug>[\w|\-]+)/delete/$', PostDeleteView.as_view(), name='post-delete'),


	url(r'^add_category/', login_required(views.add_category), name='add_category'),
	url(r'^(?P<slug>[\w|\-]+)/$', views.post, name='post'),

	url(r'^category/(?P<category_name_slug>[\w\-]+)/$', views.category, name='category'),
	
]