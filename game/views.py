# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

def game(request):
    return render(request, 'game/game/index.html')

def scoreboard(request):
    return render(request, 'game/scoreboard.html')
