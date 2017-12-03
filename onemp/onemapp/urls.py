from django.conf.urls import url
from . import views

urlpatterns = [
    #/
    url(r'^$', views.post_list, name='post_list'),
    # ex: /5/
    url(r'^(?P<post_id>[0-9]+)/$', views.post_detail, name='post_detail'),
    url(r'^my/$', views.user_post_list, name='user_post_list'),
    #/create/
    url(r'^create/$', views.post_create, name="post_create"), 
    url(r'^login/$', login,
        {
            'template_name': 'login.html',
            'authentication_form': forms.BootstrapAuthenticationForm,
            'extra_context': {'title': 'Log in', }
        },
        name='login/'),
    url(r'^logout/$', logout, {'next_page': '/', }, name='logout'),
    url(r'^register/$', forms.RegisterForm.as_view(), name='register'),
]