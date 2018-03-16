from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^scoreboard/$', views.scoreboard, name='scoreboard'),
    url(r'^$', views.game, name='game'),
]
