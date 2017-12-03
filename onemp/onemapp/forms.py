from .models import Comment


class Comment(models.Model):
    post = models.ForeignKey('Post')
    author = models.ForignKey('auth.User')
    text = models.textField()
    created_date = models.DateTimeField(default=timezone.now)
    updated_date = models.DateTimeField(default=timezone.now)
    
class CommentForm(forms.Form):
    author = forms.CharField(widget=forms.TextInput({'size': 50}), max_length=20)
    author.label = "Автор"
    text = forms.CharField(widget=forms.Textarea({'maxlength': 125, 'cols': '52', 'rows': '3'}))
    text.label = "Комментарий"

    
class PostListForm(forms.Form):
    search = forms.CharField(required=False)
    sort_field = forms.ChoiceField(choices=(('id', 'ID'), ('title', 'title'), ('-created_date', u'Дата создания')), required=False)