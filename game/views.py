# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

def scoreboard(request):
    return render(request, 'game/scoreboard.html')
