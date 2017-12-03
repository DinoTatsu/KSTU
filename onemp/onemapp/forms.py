from django import forms
from .models import Post, Comment
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.utils.translation import ugettext_lazy as _
from django.views.generic.edit import FormView


class BootstrapAuthenticationForm(AuthenticationForm):
    """Authentication form which uses boostrap CSS."""
    username = forms.CharField(max_length=254,
                               widget=forms.TextInput({'class': 'form-control', 'placeholder': 'User name'}))
    password = forms.CharField(label=_("Password"),
                               widget=forms.PasswordInput({'class': 'form-control', 'placeholder': 'Password'}))

class RegisterForm(FormView):
    form_class = UserCreationForm
    success_url = "/login/"
    template_name = "register.html"

    def form_valid(self, form):
        # Создаём пользователя, если данные в форму были введены корректно.
        form.save()

        # Вызываем метод базового класса
        return super(RegisterForm, self).form_valid(form)

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
    
    
class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = [
            "title",
            "text"
        ]