from django.conf.urls import url
from django.contrib.auth.decorators import login_required

from . import views

urlpatterns = [
    url(r'^$', login_required(views.Invest.as_view()), name='invest'),
    url(r'^itemshop/$', views.itemshop, name='itemshop'),
    url(r'^exchange_bitcoin/(?P<rate>\d+\.\d+)/$', views.exchange_bitcoin_for_in_game_currency, name='exchange_bitcoin'),
    url(r'^exchange_in_game/(?P<rate>\d+\.\d+)/$', views.exchange_in_game_currency_for_bitcoin, name='exchange_in_game'),
]
