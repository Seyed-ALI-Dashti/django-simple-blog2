from django.shortcuts import render, get_object_or_404
from . models import Blog
# Create your views here.


def index(request):
    all_blogs = Blog.objects.all()
    context = {'blogs': all_blogs}
    return render(request, 'blog/index.html', context)


def blog(request, blog_id):
    one_blog = get_object_or_404(Blog, pk=blog_id)
    context = {'blog': one_blog}
    return render(request, 'blog/blog.html', context)
