# -*- coding: utf-8 -*-
from django import forms
from django.contrib.auth.models import User
from main.models import Category, Post, Vote, Comment
from embed_video.fields import EmbedVideoField
#from django_select2 import fields, widgets, AutoModelSelect2TagField
from django_select2.forms import Select2Widget

class CategoryForm(forms.ModelForm):
	name = forms.CharField(max_length=128, label="커뮤니티 이름")
	class Meta:
		model = Category
		fields =('name','description')




#class CategoryChoices(fields.AutoModelSelect2TagField):
#	quareyset = Category.objects
#	search_fields = ['word_icontains'.]

class PostForm(forms.ModelForm):

#	category = CategoryChoices()

	title = forms.CharField(max_length=128, label="제목")

	url = forms.URLField(max_length=200,
						 help_text="기사주소를 붙여 넣어주세요", required=False, label="주소")
	views = forms.IntegerField(widget=forms.HiddenInput(), initial=0)
	class Meta:
		model = Post
		widgets = {
			'category':Select2Widget,
		}
		exclude = ['pub_date', 'moderator', 'rank_score','slug', 'image', 'thumbnail']



class ContactForm(forms.Form):
	full_name = forms.CharField(required=False)
	email = forms.EmailField()
	message = forms.CharField()


