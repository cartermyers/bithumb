# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect

from bitcoin_price_api.exchanges import CoinDesk
from observer.models import Observer

class Invest(Observer):

    def __init__(self):
        super(Invest, self).__init__()
        self.set_subject(CoinDesk())

    def get(self, request):
        #get the user's bank account info
        account = request.user.get_bank_account()
        #only show
        #and get the current bitcoin exchange rate (based on USD)
        exchange_rate = CoinDesk().get_state()['price']

        return render(request, 'invest/invest.html', {"account": account, "exchange_rate": exchange_rate, "subject": self.get_subject()})

def itemshop(request):
    return render(request, 'invest/itemshop.html')

@login_required
def exchange_bitcoin_for_in_game_currency(request):
    if request.method == "POST":
        bitcoin_amount = request.POST.get('bitcoin')
        rate = request.POSR.get('rate')

        account = request.user.get_bank_account()

        try:
            account.exchange_bitcoin_for_in_game_currency(bitcoin_amount, rate)
        except AssertionError:
            #show error here
            pass

    return HttpResponseRedirect('invest:invest')

@login_required
def exchange_in_game_currency_for_bitcoin(request):
    if request.method == "POST":
        in_game_amount = request.POST.get('in_game_currency')
        rate = request.POST.get('rate')

        account = request.user.get_bank_account()

        try:
            account.exchange_bitcoin_for_in_game_currency(in_game_amount, rate)
        except AssertionError:
            #show error here
            pass

    return HttpResponseRedirect('invest:invest')
