##from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse
from .models import Post

def post_list(request):
    posts = Post.objects.all()
    return render(request, 'post_list.html', {'posts': posts})

def post_detail(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    return render(request, 'post.html', {'post': post})
    #return render(request, 'detail.html', {'post': post})