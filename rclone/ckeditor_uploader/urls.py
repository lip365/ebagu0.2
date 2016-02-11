from __future__ import absolute_import

import django
from django.conf.urls import url
from django.views.decorators.cache import never_cache

from . import views

if django.VERSION >= (1, 8):
    urlpatterns = [
        url(r'^upload/', views.upload, name='ckeditor_upload'),
        url(r'^browse/', never_cache(views.browse), name='ckeditor_browse'),
    ]
else:
    from django.conf.urls import patterns
    urlpatterns = patterns(
        '',
        url(r'^upload/', views.upload, name='ckeditor_upload'),
        url(r'^browse/', never_cache(views.browse), name='ckeditor_browse'),
    )
