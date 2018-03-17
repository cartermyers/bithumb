# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from account.models import User

def scoreboard(request):
    #get top 10 users by high score
    top_users = User.objects.order_by('highscore')[:10]
    return render(request, 'game/scoreboard.html', {'top_users': top_users})
