from django.utils import timezone
from .models import Post
from django.shortcuts import render

def post_list(request):
    posts = Post.objects.all()
    return render(request, 'blog/post_list.html', {'posts': posts})
