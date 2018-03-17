# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.contrib.auth.decorators import login_required

def game(request):
    return render(request, 'game/game/index.html')

def scoreboard(request):
    return render(request, 'game/scoreboard.html')

@login_required
def temp_send_page(request):
    return render(request, 'invest/send_temp.html', {'money': request.user.bank_account.get_in_game_currency()})

@login_required
def send_score(request):
    if request.method == "POST":
        #get the user's bank account
        account = request.user.get_bank_account()

        #update the in-game currency:
        account.deposit_in_game_currency(request.POST.get('score', 0))
        account.save()

        #return success with new amount for user
        return HttpResponse(
        dumps({'new_amount': account.get_in_game_currency()}),
        content_type='application/json')
    else:
        return HttpResponse(
        dumps({'response': 'This is only supported with POST methods'}),
        content_type='application/json')
