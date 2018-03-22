# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.decorators import login_required

from json import dumps

from account.models import User

@login_required
def game(request):
    return render(request, 'game/game.html')

def scoreboard(request):
    #get top 10 users by high score
    top_users = User.objects.order_by('-highscore')[:10]
    return render(request, 'game/scoreboard.html', {'top_users': top_users})

@login_required
def send_score(request):
    if request.method == "POST":
        #get the user's bank account
        account = request.user.get_bank_account()

        #update the in-game currency:
        new_score = request.POST.get('score', 0)

        if new_score < 0:
            new_score = 0

        account.deposit_in_game_currency(new_score)
        account.save()

        #return success with new amount for user
        return HttpResponse(
        dumps({'new_amount': account.get_in_game_currency()}),
        content_type='application/json')
    else:
        return HttpResponse(
        dumps({'response': 'This is only supported with POST methods'}),
        content_type='application/json')
