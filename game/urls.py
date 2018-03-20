from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.play_game, name='play_game'),
    url(r'^game$', views.game, name='game'),
    url(r'^scoreboard/$', views.scoreboard, name='scoreboard'),
    url(r'^send_score/$', views.send_score, name='send_score'),
]
