from django.conf.urls import patterns, url
	
urlpatterns = patterns(
    '',
	url(r'^accounts/(?P<username>[\.\w-]+)/edit/$', 'userena.views.profile_edit', {'edit_profile_form': EditProfileFormExtra}, name='userena_profile_edit'),
    
)

