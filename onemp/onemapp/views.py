##from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse
from .models import Post

def post_list(request):
    """ Список всех постов с возможностью сортировки и поиска по title, можно добавить пост"""
    if user and user.is_authenticated:
        posts = Post.objects.filter(author=user)  # получить посты пользователя
    else:
        posts = Post.objects.all()  # получить все посты

    form = PostListForm(request.GET)  # создать форму на основе модели Post
    form.is_valid()
    if form.cleaned_data.get('search'):
        posts = posts.filter(title__icontains=form.cleaned_data['search'])
    if form.cleaned_data.get('sort_field'):
        posts = posts.order_by(form.cleaned_data['sort_field'])

    for post in posts:
        post.text = post.text[:50]
    return render(request, 'post_list.html', {'form': form, 'posts': posts})


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