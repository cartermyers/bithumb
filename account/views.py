# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

def signup(request):
    return render(request, 'account/signup.html')

def profile(request, user_id):
    #do the query here
    return render(request, 'account/profile.html')
