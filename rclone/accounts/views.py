from django.shortcuts import render

# Create your views here.
@receiver(post_save, sender=User, dispatch_uid='user.created')
def user_created(sender, instance, created, raw, using, **kwargs):
  """ Adds 'change_profile' permission to created user objects """
  if created:
    from guardian.shortcuts import assign
    assign('change_profile', instance, instance.get_profile())


    