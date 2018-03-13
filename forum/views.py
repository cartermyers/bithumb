# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.urls import reverse

from . import forms, models

def all_forums(request):
    return render(request, 'forum/all_forums.html')

def forum(request, forum_id):
    forum = get_object_or_404(models.Forum, pk=forum_id)

    return render(request, 'forum/forum.html', {'forum': forum})

@login_required
def post_forum(request):

    if request.method == "POST":
        form = forms.ForumForm(request.POST)
        if form.is_valid():
            new_post = form.save(commit=False)
            new_post.set_poster(request.user)
            new_post.save()

            return HttpResponseRedirect(reverse('forum:forum', kwargs={'forum_id': new_post.pk}))
    else:
        form = forms.ForumForm()

    return render(request, 'forum/new_forum.html', {'form': form})
