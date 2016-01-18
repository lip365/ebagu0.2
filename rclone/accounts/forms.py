from userena.forms import EditProfileForm

class EditProfileFormExtra(EditProfileForm):
    class Meta:
      exclude = ['privacy']