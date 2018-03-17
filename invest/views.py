# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.decorators import login_required

from . import models

@login_required
def invest(request):
    if request.method == "POST":
        #TODO
        #handle the investments here
        pass
    else:
        #get the user's bank account info
        account = request.user.get_bank_account()
        #and get the current bitcoin exchange rate:
        #TODO

    return render(request, 'invest/invest.html', {"account": account})

def itemshop(request):
    return render(request, 'invest/itemshop.html')
