from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import include, url
from django.contrib import admin
from django.conf.urls import patterns, url
from envelope.views import ContactView
from django.contrib.auth.decorators import login_required as auth
from main import views
from tastypie.api import Api


urlpatterns = [
	url(r'^admin/', include(admin.site.urls)),
	url(r'^contact/', include('envelope.urls')),
	url(r'^select2/', include('django_select2.urls')),
	url(r'^activity/', include('actstream.urls')),
	url(r'^ckeditor/', include('ckeditor_uploader.urls')),
	#url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': MEDIA_ROOT}),
	url(r'^main/search/',include('haystack.urls')),

    url(r'^accounts/(?P<username>[\.\w-]+)/edit/$',views.profile_edit,
       name='userena_profile_edit'),
	url(r'^accounts/', include('userena.urls')),

	url(r'^', include('main.urls')),



]
if settings.DEBUG:
	urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
	urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)