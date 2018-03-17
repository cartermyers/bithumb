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

    def post(request):
        #TODO
        #handle the investments here
        #then return to same page to show new investments

        return HttpResponseRedirect('invest:invest')

    def get(self, request):
        #get the user's bank account info
        account = request.user.get_bank_account()
        #only show
        #and get the current bitcoin exchange rate (based on USD)
        exchange_rate = CoinDesk().get_state()['price']

        return render(request, 'invest/invest.html', {"account": account, "exchange_rate": exchange_rate, "subject": self.get_subject()})

def itemshop(request):
    return render(request, 'invest/itemshop.html')
