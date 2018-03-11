from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^signup/$', views.signup, name='signup'),
    url(r'^(?P<user_id>[0-9]+)/$', views.profile, name='profile'),
]
