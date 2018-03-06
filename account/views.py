# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.contrib.auth import login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.hashers import make_password

from . import forms, models

def signup(request):
    if request.method == 'POST' and not request.user.is_authenticated:
        form = forms.UserForm(request.POST)

        if form.is_valid():
            #save the new object
            new_user = form.save(commit=False)
            new_user.set_password(make_password(form.cleaned_data['password']))
            new_user.save()

            #login the new user
            login(request, new_user)

            #redirect to profile
            return HttpResponseRedirect(reverse('account:myprofile'))
    else:
        form = forms.UserForm()

    return render(request, 'account/signup.html', {'form': form})

def profile(request, user_id=None):
    if user_id == None and request.user.is_authenticated:
        user_id = request.user.pk

    user = get_object_or_404(models.User, pk=user_id)

    return render(request, 'account/profile.html', {'user_profile': user})

def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))
