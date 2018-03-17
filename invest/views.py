# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.decorators import login_required

from . import models

def invest(request):
    return render(request, 'invest/invest.html')

def itemshop(request):
    return render(request, 'invest/itemshop.html')
