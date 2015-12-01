from django.conf.urls import url
from main import views

urlpatterns = [
	url(r'^$', views.index, name='index'),
	url(r'^add_post/', views.add_post, name='add_post'),

	url(r'^add_category/', views.add_category, name='add_category'),
	url(r'^(?P<slug>[\w|\-]+)/$', views.post, name='post'),

	url(r'^category/(?P<category_name_slug>[\w\-]+)/$', views.category, name='category'),
]