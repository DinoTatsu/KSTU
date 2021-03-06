from django.db import models
from django.utils import timezone

class PostFile(models.Model):
    description = models.CharField(max_length=255, blank=True)
    file = models.FileField(upload_to='files/')

class Post(models.Model):
    author = models.ForeignKey('auth.User')
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    file = models.URLField(null=True)

    def __str__(self):
        return self.title


class Comment(models.Model):
    title = models.CharField(max_length=25, default="")
    author = models.CharField(max_length=20)
    text = models.CharField(max_length=140)
    created_date = models.DateTimeField(default=timezone.now)
    post = models.ForeignKey(Post)

    def __str__(self):
        return self.title
