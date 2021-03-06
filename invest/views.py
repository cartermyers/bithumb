# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib import messages
from django.urls import reverse
from decimal import Decimal

from bitcoin_price_api.exchanges import CoinDesk
from observer.models import Observer

from . import forms
from . import models

class Invest(Observer):

    def __init__(self):
        super(Invest, self).__init__()
        self.set_subject(CoinDesk())

    #this is the display function in the Observer pattern pseudocode
    # it's named as "get" to comply with Django functionality
    def get(self, request, bitcoin_form = forms.BitcoinToInGameCurrencyForm(), in_game_currency_form = forms.InGameCurrencyToBitcoinForm()):

        #get the user's bank account info
        account = request.user.get_bank_account()
        #only show
        #and get the current bitcoin exchange rate (based on USD)
        exchange_rate = CoinDesk().get_state()['price']

        return render(request, 'invest/invest.html', {"account": account, "exchange_rate": exchange_rate, \
                "subject": self.get_subject(), "bitcoin_form": bitcoin_form, "in_game_currency_form": in_game_currency_form})

def itemshop(request):
    trophies = models.Collectible.objects.all()
    owned = None
    balance = None

    if request.user.is_authenticated:
        owned = request.user.get_collectibles()
        balance = request.user.get_bank_account().get_in_game_currency()

        #validate the form here
        if request.method == "POST":
            #make sure the collectible exists:
            try:
                collectible = models.Collectible.objects.get(pk=int(request.POST['trophy']))
            except models.Collectible.DoesNotExist:
                message.error(request, "Item does not exist.")

            #make sure the user doesn't own it
            if collectible in owned:
                messages.error(request, "You already own this item.")

            try:
                request.user.buy_collectible(collectible)
                #and add the new objects for the view
                owned.append(collectible)
                balance -= collectible.get_price()
            except AssertionError:
                messages.error(request, "You don't have enough money for this item.")

    return render(request, 'invest/itemshop.html', {'trophies': trophies, 'owned': owned, 'balance': balance})

@login_required
def exchange_bitcoin_for_in_game_currency(request):
    bitcoin_form = None
    if request.method == "POST":
        bitcoin_form = forms.BitcoinToInGameCurrencyForm(request.POST)

        if bitcoin_form.is_valid():
            account = request.user.get_bank_account()
            bitcoin = bitcoin_form.cleaned_data['bitcoin']
            rate = Decimal(CoinDesk().get_state()['price'])
            try:
                account.exchange_bitcoin_for_in_game_currency(bitcoin, rate)
                return HttpResponseRedirect(reverse('invest:invest'))
            except AssertionError:
                bitcoin_form.add_error(None, "Sorry, you don't have enough in your account to make that exchange.")

    #if there are any errors:
    return Invest().get(request, bitcoin_form=bitcoin_form)

@login_required
def exchange_in_game_currency_for_bitcoin(request):
    in_game_currency_form = None
    if request.method == "POST":
        in_game_currency_form = forms.InGameCurrencyToBitcoinForm(request.POST)

        if in_game_currency_form.is_valid():
            account = request.user.get_bank_account()
            in_game_currency = in_game_currency_form.cleaned_data['in_game_currency']
            rate = Decimal(CoinDesk().get_state()['price'])
            try:
                account.exchange_in_game_currency_for_bitcoin(in_game_currency, rate)
                return HttpResponseRedirect(reverse('invest:invest'))
            except AssertionError:
                in_game_currency_form.add_error(None, "Sorry, you don't have enough in your account to make that exchange.")


    #if there are any errors:
    return Invest().get(request, in_game_currency_form=in_game_currency_form)
