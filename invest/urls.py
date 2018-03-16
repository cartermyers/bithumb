from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.invest, name='invest'),
    url(r'^itemshop/$', views.itemshop, name='itemshop'),
    url(r'^send_score/$', views.send_score, name='send_score'),
    url(r'^temp_send_page/$', views.temp_send_page, name='temp_send_page'),
]
