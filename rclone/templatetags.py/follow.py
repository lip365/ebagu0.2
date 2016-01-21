
from actstream.models import following
from django.contrib.auth.models import User
from django.template import Library

register = Library()


# @register.filter
# def follows(follower, followee):
#     return followee in following(follower, User)