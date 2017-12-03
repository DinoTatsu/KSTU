##from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse
from .models import Post

def post_list(request):
    posts = Post.objects.all()
    return render(request, 'post_list.html', {'posts': posts})

def post_detail(request, post_id):
    """ Пост с комментариями, можно добавить комментарий"""
    post = get_object_or_404(Post, pk=post_id)
    comments = Comment.objects.filter(post=post)
    form = CommentForm(request.POST)
    form.is_valid()
    if form.cleaned_data.get('author') and form.cleaned_data.get('text'):
        author = form.cleaned_data.get('author')
        text = form.cleaned_data.get('text')[:125]
        title = text[:25]
        comment = Comment.objects.create(title=title, post=post, author=author, text=text)
    return render(request, 'post.html', {'post': post, 'comments': comments, 'form': form})