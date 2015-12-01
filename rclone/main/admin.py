from django.contrib import admin
from main.models import Post, Category
# Register your models here.

class PageAdmin(admin.ModelAdmin):
	list_display = ('title', 'category')

class CatAdmin(admin.ModelAdmin): 
	
	prepopulated_fields = {'slug':('name',)}
	fields = ['name', 'slug']

admin.site.register(Post, PageAdmin)
admin.site.register(Category, CatAdmin)