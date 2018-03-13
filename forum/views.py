# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, get_object_or_404

from .models import Forum, Comments

def all_forums(request):
    return render(request, 'forum/all_forums.html')

def forum(request, forum_id):
    forum = get_object_or_404(Forum, pk=forum_id)

    return render(request, 'forum/forum.html', {'forum': forum})
