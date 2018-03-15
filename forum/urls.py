
from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.all_forums, name='all_forums'),
    url(r'^(?P<forum_id>[0-9]+)/$', views.forum, name='forum'),
    url(r'^post/$', views.post_forum, name='post'),
    url(r'^delete_comment/(?P<comment_id>[0-9]+)$', views.delete_comment, name='delete_comment'),
    url(r'^delete_forum/(?P<forum_id>[0-9]+)$', views.delete_forum, name='delete_forum'),
]
