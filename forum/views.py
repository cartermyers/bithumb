# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from . import forms, models

def all_forums(request):

    forum_list = models.Forum.objects.all().order_by('-time')
    items_per_page = 10

    page_list = Paginator(forum_list, items_per_page)

    """ Here is some code from https://docs.djangoproject.com/en/1.11/topics/pagination/ """
    current_page = request.GET.get('page', None)
    try:
        forums = page_list.page(current_page)
        current_page = int(current_page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        forums = page_list.page(1)
        current_page = 1
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        forums = page_list.page(page_list.num_pages)
        current_page = page_list.num_pages

    # do some calculations to find a number of next pages
    start_page = max(0, current_page - 3)
    end_page = min(page_list.num_pages, current_page + 3)
    page_range = range(start_page + 1, end_page + 1)

    return render(request, 'forum/all_forums.html', {'forums': forums, 'current_page': current_page, 'page_range': page_range})

#This also handles the comment posting
def forum(request, forum_id):
    forum = get_object_or_404(models.Forum, pk=forum_id)

    if request.method == "POST" and request.user.is_authenticated:
        comment_form = forms.CommentForm(request.POST)

        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.set_user(request.user)
            new_comment.set_post(forum)
            new_comment.save()

            #after saving the comment, return back to the same page
            return HttpResponseRedirect(reverse('forum:forum', kwargs={'forum_id':forum_id}))
    else:
        comment_form = forms.CommentForm()

    return render(request, 'forum/forum.html', {'forum': forum, 'comment_form': comment_form})

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

    return render(request, 'forum/new_forum.html', {'forum_form': form})

@login_required
def delete_comment(request, comment_id):
    comment = models.Comments.objects.get(pk=comment_id)

    if comment.user_id == request.user.pk:
        comment.delete()

    return HttpResponseRedirect(reverse('forum:forum', kwargs={'forum_id': comment.post_id}))

@login_required
def delete_forum(request, forum_id):
    forum = models.Forum.objects.get(pk=forum_id)

    if forum.poster_id == request.user.pk:
        forum.delete()

    return HttpResponseRedirect(reverse('forum:all_forums'))
