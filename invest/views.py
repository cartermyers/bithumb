# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

def invest(request):
    return render(request, 'invest/invest.html')
