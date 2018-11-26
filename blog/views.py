from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render
from blog.models import Blog, Comment

# Create your views here.
def index(request):
	blogs = Blog.objects.all()
	first_blog = Blog.objects.get(pk=1)
	comments = Comment.objects.filter(blog=first_blog)
	return render(request, 'blog/blog.html', {'blogs': blogs, 'comments': comments,})