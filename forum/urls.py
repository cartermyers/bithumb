
from django.conf.urls import url

from . import views


urlpatterns = [
    url(r'^$', views.all_forums, name='all_forums'),
    url(r'^(?P<forum_id>[0-9]+)/$', views.forum, name='forum'),
]
