from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect 
from django.template import Context, loader,RequestContext
from django.shortcuts import get_object_or_404, render_to_response, redirect
# Create your views here.
from main.models import Post, Category
from main.forms import UserForm, UserProfileForm, CategoryForm, PostForm
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.shortcuts import render
from django.core.urlresolvers import reverse 

#for front page

def index(request):

    categories = Category.objects.order_by('likes')[:5]
    latest_posts = Post.objects.all().order_by('-created_at')
    popular_posts = Post.objects.all().order_by('-views')
    hot_posts = Post.objects.all().order_by('-score')[:25]

    context_dict = {
        'latest_posts': latest_posts,
        'popular_posts': popular_posts,
        'hot_posts': hot_posts,
        'categories': categories
    }
    return render(request, 'main/index.html', context_dict)
#for single-post page
#we use uuslug 
def post(request, slug):
    single_post = get_object_or_404(Post, slug=slug)
    single_post.views += 1  # increment the number of views
    single_post.save()      # and save it
    t = loader.get_template('main/post.html')
    context_dict = {
        'single_post': single_post,
    }
    c = Context(context_dict)
    return HttpResponse(t.render(c))
#for category page
#we use slugfield this time 
def category(request, category_name_slug):
	context_dict = {}
	try:
		category = Category.objects.get(slug=category_name_slug)
		context_dict['category_name'] = category.name

		posts = Post.objects.filter(category=category)
		context_dict['posts'] = posts
		context_dict['category'] = category
	except Category.DoesNotExist:
		pass

	return render(request, 'main/category.html', context_dict)
#for adding category
def add_category(request):
	if request.method == 'POST':
		form = CategoryForm(request.POST)
		if form.is_valid():
			form.save(commit=True)
			return index(request)
		else:
			print form.errors
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

