# -*- coding: utf-8 -*-

from django.contrib import admin
from main.models import Post, Category, Vote
# Register your models here.

class PageAdmin(admin.ModelAdmin):
	list_display = ('title', 'category')

admin.site.register(Post, PageAdmin)
admin.site.register(Category)
