from userena import views as userena_views
from userena.utils import get_profile_model

class CustomEditProfileForm(userena_views.EditProfileForm):
    """ Base form used for fields that are always required """
   
    class Meta:
        model = get_profile_model()
        exclude = ['user', 'privacy']
