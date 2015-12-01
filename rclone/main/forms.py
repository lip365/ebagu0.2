# -*- coding: utf-8 -*- 
from django import forms
from django.contrib.auth.models import User
from main.models import Category, Post, UserProfile


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
	name = forms.CharField(max_length=128, help_text="커뮤니티 이름을 적어주세요")
	likes = forms.IntegerField(widget=forms.HiddenInput(), initial=0)
	slug = forms.CharField(widget=forms.HiddenInput, required=False)

	class Meta:
		model = Category
		fields =('name',)

class PostForm(forms.ModelForm):
	title = forms.CharField(max_length=128, help_text="제목을 입력해주세요")
	views = forms.IntegerField(widget=forms.HiddenInput(), initial=0)
	class Meta:
		model = Post
		fields = ['title', 'content', 'image', 'views', 'category']