from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^scoreboard/$', views.scoreboard, name='scoreboard'),
    url(r'^$', views.game, name='game'),
    url(r'^send_score/$', views.send_score, name='send_score'),
    url(r'^temp_send_page/$', views.temp_send_page, name='temp_send_page'),
]
