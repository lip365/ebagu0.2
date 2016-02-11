# -*- coding: utf-8 -*-

from django.contrib import admin
from main.models import Post, Category, Comment

admin.site.register(Post)
admin.site.register(Category)
admin.site.register(Comment)
