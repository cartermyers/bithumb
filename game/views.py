# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

def main_game(request):
    return render(request, 'game/main_game.html')
