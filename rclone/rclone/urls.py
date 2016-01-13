from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import include, url
from django.contrib import admin
from django.conf.urls import patterns, url
from envelope.views import ContactView
from django.contrib.auth.decorators import login_required as auth

urlpatterns = [
	url(r'^admin/', include(admin.site.urls)),
	url(r'^contact/', include('envelope.urls')),

	url(r'^froala_editor/', include('froala_editor.urls')),
   
	#url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': MEDIA_ROOT}),
	url(r'^search/$',include('haystack.urls')),
	url(r'^favorites/', include('favorites.urls')),


	url(r'^accounts/', include('userena.urls')),
	url(r'^', include('main.urls')),


]

if settings.DEBUG:
	urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
	urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)