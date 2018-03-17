# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect

from bitcoin_price_api.exchanges import CoinDesk

@login_required
def invest(request):
    if request.method == "POST":
        #TODO
        #handle the investments here
        #then return to same page to show new investments

        return HttpResponseRedirect('invest:invest')
    else:
        #get the user's bank account info
        account = request.user.get_bank_account()
        #only show
        #and get the current bitcoin exchange rate (based on USD)
        exchange_rate = CoinDesk().get_state()

    return render(request, 'invest/invest.html', {"account": account, "exchange_rate": exchange_rate})

def itemshop(request):
    return render(request, 'invest/itemshop.html')
