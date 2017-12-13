from django.shortcuts import get_object_or_404, render, redirect, resolve_url
from django.http import HttpResponse
from django.contrib.auth import get_user
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .models import Post, Comment
from .forms import PostListForm, PostForm, CommentForm, BootstrapAuthenticationForm, FileForm
from django.core.files.storage import FileSystemStorage


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


@login_required
def user_post_list(request):
    user = get_user(request)
    return post_list(request, user)


def post_list(request, user=None):
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


def simple_upload(request):
    if request.method == 'POST' and request.FILES['myfile']:
        myfile = request.FILES['myfile']
        fs = FileSystemStorage()
        filename = fs.save(myfile.name, myfile)
        uploaded_file_url = fs.url(filename)
        return render(request, 'file_upload.html', {
            'uploaded_file_url': uploaded_file_url
        })
    return render(request, 'file_upload.html')


@login_required
def post_create(request):
    """ Добавление поста"""
    user = get_user(request)
    form = PostForm(request.POST, request.FILES)
    form.is_valid()
    title = form.cleaned_data.get('title')
    text = form.cleaned_data.get('text')
    if title and text:
        if request.FILES['myfile']:
            file = request.FILES.get("myfile") #["myfile"]
            fs = FileSystemStorage()
            filename = fs.save(file.name, file)
            file_url = fs.url(filename)
            post = Post.objects.create(title=title, text=text, author=user, file=file_url)
        else:
            post = Post.objects.create(title=title, text=text, author=user)
        return redirect(post_detail, post.pk)
    return render(request, 'post_form.html', {'form': form})


def model_form_upload(request):
    if request.method == 'POST':
        form2 = FileForm(request.POST, request.FILES)
        if form2.is_valid():
            form2.save()
            return redirect('post_list')
    else:
        form2 = FileForm()
    return render(request, 'file_upload2.html', {
        'form': form2
    })