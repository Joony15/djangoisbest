from django.contrib import admin
from blog.models import Post
from blog.forms import PostForm
# Register your models here.


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    form = PostForm
    list_display = ['id', 'title']  
    list_display_links = ['title'] 
