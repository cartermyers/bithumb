from django.conf.urls import url
from django.contrib.auth.decorators import login_required

from . import views

urlpatterns = [
    url(r'^$', login_required(views.Invest.as_view()), name='invest'),
    url(r'^itemshop/$', views.itemshop, name='itemshop'),
]
