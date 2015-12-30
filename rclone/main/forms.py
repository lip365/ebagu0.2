# -*- coding: utf-8 -*-
from django import forms
from django.contrib.auth.models import User
from main.models import Category, Post, UserProfile, Vote
from froala_editor.widgets import FroalaEditor


class UserForm(forms.ModelForm):
	password = forms.CharField(widget=forms.PasswordInput())

	class Meta:
		model = User
		fields = ('username', 'email', 'password')

class UserProfileForm(forms.ModelForm):

	class Meta:
		model = UserProfile
		fields = ('website', 'picture')

class CategoryForm(forms.ModelForm):
	name = forms.CharField(max_length=128, help_text="plz enter")
	likes = forms.IntegerField(widget=forms.HiddenInput(), initial=0)
	slug = forms.CharField(widget=forms.HiddenInput, required=False)

	class Meta:
		model = Category
		fields =('name',)

class PostForm(forms.ModelForm):
	title = forms.CharField(max_length=128, help_text="plz enter")

	url = forms.URLField(max_length=200,
						 help_text="Please enter the URL of the page.", required=False)
	views = forms.IntegerField(widget=forms.HiddenInput(), initial=0)
	content = forms.CharField(widget=FroalaEditor)
	class Meta:
		model = Post

		exclude = ['pub_date', 'moderator', 'rank_score', 'image','slug']



class ContactForm(forms.Form):
	full_name = forms.CharField(required=False)
	email = forms.EmailField()
	message = forms.CharField()
