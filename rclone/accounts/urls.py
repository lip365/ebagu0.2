'''
from django.conf.urls import patterns, url
from accounts.forms import EditProfileFormExtra
	
urlpatterns = patterns(
    '',
url(r'^(?P<username>[\.\w-]+)/edit/$', 'userena.views.profile_edit', {'edit_profile_form': EditProfileFormExtra}, name='edit-profile'),

   
    
)

'''