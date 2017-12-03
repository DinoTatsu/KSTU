##from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404, render, redirect, resolve_url
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .models import Post, Comment
from .forms import PostListForm, PostForm, CommentForm, BootstrapAuthenticationForm



@login_required
def user_post_list(request):
    user = get_user(request)
    return post_list(request, user)

    
def post_list(request):
    """ ������ ���� ������ � ������������ ���������� � ������ �� title, ����� �������� ����"""
    if user and user.is_authenticated:
        posts = Post.objects.filter(author=user)  # �������� ����� ������������
    else:
        posts = Post.objects.all()  # �������� ��� �����

    form = PostListForm(request.GET)  # ������� ����� �� ������ ������ Post
    form.is_valid()
    if form.cleaned_data.get('search'):
        posts = posts.filter(title__icontains=form.cleaned_data['search'])
    if form.cleaned_data.get('sort_field'):
        posts = posts.order_by(form.cleaned_data['sort_field'])

    for post in posts:
        post.text = post.text[:50]
    return render(request, 'post_list.html', {'form': form, 'posts': posts})


def post_detail(request, post_id):
    """ ���� � �������������, ����� �������� �����������"""
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
    

@login_required
def post_create(request):
    """ ���������� �����"""
    user = get_user(request)
    form = PostForm(request.POST)
    form.is_valid()
    title = form.cleaned_data.get('title')
    text = form.cleaned_data.get('text')
    if title and text:
        post = Post.objects.create(title=title, text=text, author=user)
        return redirect(post_detail, post.pk)
    return render(request, 'post_form.html', {'form': form})