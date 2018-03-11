# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

def all_forums(request):
    return render(request, 'forum/all_forums.html')
