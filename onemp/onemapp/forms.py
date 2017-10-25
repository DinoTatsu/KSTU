from .models import Comment

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('text')
        
class Comment(models.Model):
    post = models.ForeignKey('Post')
    author = models.ForignKey('auth.User')
    text = models.textField()
    created_date = models.DateTimeField(default=timezone.now)
    updated_date = models.DateTimeField(default=timezone.now)
    