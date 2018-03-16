# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
#from django.auth.contrib.decorators import login_required

#@login_required
#this is the actual game used for the iframe
def game(request):
    return render(request, 'game/game.html')

#@login_required
#this is the actual page where players should be directed
def play_game(request):
    return render(request, 'game/index.html')

def scoreboard(request):
    return render(request, 'game/scoreboard.html')
