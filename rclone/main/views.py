# -*- coding: utf-8 -*-
import json
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, HttpResponseBadRequest 
from django.template import Context, loader,RequestContext
from django.shortcuts import get_object_or_404, render_to_response, redirect
# Create your views here.
from main.models import Post, Category, Vote
from main.forms import UserForm, UserProfileForm, CategoryForm, PostForm
from django.views.generic.edit import CreateView, UpdateView, DeleteView, FormView
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.shortcuts import render
from django.core.urlresolvers import reverse 
from django.core.paginator import Paginator
from main.util.common import SortMethods
from main.util.media import extract
from haystack.query import SearchQuerySet
#for front page

def index(request):
		categories = Category.objects.all()
		
		try:
				sort = request.GET["sort"].strip()
				sort_method = SortMethods[sort]
				page = request.GET["page"].strip()
		except KeyError:
				sort_method = SortMethods.score
				page = 1

		if sort_method == SortMethods.date:
				post_list = Post.objects.order_by("-pub_date")
		else:
				post_list = Post.objects.all()
				post_list = sorted(post_list, key=lambda x: x.get_score(), reverse=True)

		paginator = Paginator(post_list, 30)

		try:
				posts = paginator.page(page)
		except PageNotAnInteger:
				posts = paginator.page(1)
		except EmptyPage:
				posts = paginator.page(paginator.num_pages)

		context = {
				"posts": posts,
				"pages": paginator.page_range,
				"sort": sort_method.name,
				"categories":categories,

		}
		return render(request, "main/index.html", context)

#for single-post page
def post(request, slug):
		post = get_object_or_404(Post, slug=slug)
		post.views += 1  # increment the number of views
		post.save()      # and save it
		context_dict = {
			'post' :post,
		}
	
		return render(request, 'main/post.html', context_dict)
#for category page
def category(request, category_name_slug):
	try:
		
				category = Category.objects.get(slug=category_name_slug)
				sort = request.GET["sort"].strip()
				sort_method = SortMethods[sort]
				page = request.GET["page"].strip()
	except KeyError:
				sort_method = SortMethods.score
				page = 1

	if sort_method == SortMethods.date:
				thread_list = Post.objects.filter(category=category).order_by("-pub_date")
	else:
				thread_list = Post.objects.filter(category=category)
				thread_list = sorted(thread_list, key=lambda x: x.get_score(), reverse=True)

	paginator = Paginator(thread_list, 30)

	try:
				posts = paginator.page(page)
	except PageNotAnInteger:
				posts = paginator.page(1)
	except EmptyPage:
				posts = paginator.page(paginator.num_pages)
	
	if request.method == 'POST':
		query = request.POST.get('query')
		if query:
			query = query.strip()
			result_list = run_query(query)

	context = {
				"posts": posts,
				"pages": paginator.page_range,
				"sort": sort_method.name,
				"categories":category,
			  "cat_name_slug":category_name_slug,
			  "result_list":result_list,
		}
	return render(request, "main/index.html", context)


@login_required
def add_category(request):
	if Category.objects.filter(author=request.user).exists():
		if request.method == 'POST':
			category = Category(author=request.user)
			form = CategoryForm(request.POST, instance=category)
			if form.is_valid():
				form.save(commit=True)
				return index(request)
			
		else:
			form = CategoryForm()

	return render(request, 'main/add_category.html', {'form':form})



class PostCreateView(CreateView):

	 model = Post
	 form_class = PostForm
	 template_name = 'main/add_post.html'
	
	 def form_valid(self, form):
			self.object = form.save(commit=False)
			# any manual settings go here
			self.object.moderator = self.request.user
			self.object.image = extract(self.object.url) 

			self.object.save()
			return HttpResponseRedirect(reverse('post', args=[self.object.slug]))

	 @method_decorator(login_required)
	 def dispatch(self, request, *args, **kwargs):
		
			return super(PostCreateView, self).dispatch(request, *args, **kwargs)
	


class PostUpdateView(UpdateView):
	 model = Post
	 form_class = PostForm
	 template_name = 'main/edit.html'

	 def form_valid(self, form):
			self.object = form.save(commit=False)
			# Any manual settings go here
			self.object.save()
			return HttpResponseRedirect(self.object.get_absolute_url())

	 @method_decorator(login_required)
	 def dispatch(self, request, *args, **kwargs):
		 return super(PostUpdateView, self).dispatch(request, *args, **kwargs)



class PostDeleteView(DeleteView):
	 model = Post

	 def get_success_url(self):
			return "/" 

	 @method_decorator(login_required)
	 def dispatch(self, request, *args, **kwargs):
			return super(PostDeleteView, self).dispatch(request, *args, **kwargs)



def vote(request, slug):
		"""This view is intended to use ajax and handle vote.
		Checking GET parameter 'is_up' decide upvote or devote.
		:param request: Django request object
		:param thread_id: Voted thread id
		:return: If success, sum of upvote and devote. if not, error message
		"""
		try:
				error_message = "Not a valid request"
				is_up = int(request.GET["is_up"].strip())
				if is_up == 1 or is_up == 0:
						if not request.user.is_authenticated():
								error_message = "please login"
						else:
								post = get_object_or_404(Post, slug=slug)
								try:
										vote = post.vote_set.get(user=request.user)
								except Vote.DoesNotExist:
										post.vote_set.create(user=request.user, is_up=is_up)
								else:
										if vote.is_up == is_up:
												vote.delete()
										else:
												vote.is_up = is_up
												vote.save()

								json_data = '{"count":"%s"}' % post.get_vote_count()
								return HttpResponse(json_data, content_type="application/json; charset=utf-8")
		except KeyError:
				json_data = '{"error_message":"%s"}' % "Not a valid request"
				return HttpResponseBadRequest(json_data, content_type="application/json; charset=utf-8")
		else:
				json_data = '{"error_message":"%s"}' % error_message
				return HttpResponseBadRequest(json_data, content_type="application/json; charset=utf-8")



def search_titles(request):
	articles = SearchQuerySet().autocomplete(content_auto=request.POST.get('search_text', ''))            
	
	return render_to_response('ajax_search.html', {'articles' : articles})
