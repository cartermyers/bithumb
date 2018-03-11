from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.invest, name='invest'),
    url(r'^itemshop/$', views.itemshop, name='itemshop'),
]
