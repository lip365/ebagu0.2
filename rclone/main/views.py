from django.shortcuts import render
from django.http import HttpResponse 
from django.template import Context, loader,RequestContext
from django.shortcuts import get_object_or_404, render_to_response, redirect
# Create your views here.
from main.models import Post, Category
from main.forms import UserForm, UserProfileForm, CategoryForm, PostForm

#for front page
def index(request):

	categories = Category.objects.order_by('likes')[:5]
	latest_posts = Post.objects.all().order_by('-created_at')
	popular_posts = Post.objects.all().order_by('-views')
	hot_posts = Post.objects.all().order_by('-score')[:25]

	t = loader.get_template('main/index.html')
	context_dict = {
		'latest_posts' :latest_posts,
		'popular_posts' :popular_posts,
		'hot_posts' :hot_posts,
		'categories':categories
}
	c = Context(context_dict)
	return HttpResponse(t.render(c))

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

#for adding post/see diff style :)

def add_post(request):
    context = RequestContext(request)
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():  # is the form valid?
            form.save(commit=True)  # yes? save to database
            return redirect(index)
        else:
            print form.errors  # no? display errors to end user
    else:
        form = PostForm()
    return render_to_response('main/add_post.html', {'form': form}, context)

