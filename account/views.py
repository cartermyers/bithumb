# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.contrib.auth import login, logout, authenticate
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.hashers import make_password

from . import forms, models
from invest.models import BankAccount

def signup_view(request):

    if request.user.is_authenticated:
        return HttpResponseRedirect(reverse('account:myprofile'))

    login_form = forms.LoginForm()

    if request.method == 'POST':
        signup_form = forms.SignupForm(request.POST)

        if signup_form.is_valid():
            #save the new object
            new_user = signup_form.save(commit=False)
            new_user.set_password(make_password(signup_form.cleaned_data['password']))
            new_user.save()

            #login the new user
            login(request, new_user)

            #redirect to profile
            return HttpResponseRedirect(reverse('account:myprofile'))
    else:
        signup_form = forms.SignupForm()

    return render(request, 'bithumb/index.html', {'signup_form': signup_form, 'login_form': login_form})

def login_view(request):

    # this holds where the users should be redirected to
    redirect = request.GET.get('next', reverse('index'))

    if request.user.is_authenticated:
        return HttpResponseRedirect(redirect)

    signup_form = forms.LoginForm()

    if request.method == 'POST':
        login_form = forms.LoginForm(request.POST)

        if login_form.is_valid():
            user = authenticate(request, username=login_form.cleaned_data['username'], password=login_form.cleaned_data['password'])

            # if user is not None, then there are no errors
            if user:
                login(request, user)
                if login_form.cleaned_data['keep_me_logged_in']:
                    request.session.set_expiry(60 * 60 * 24 * 10) # set expiry for 10 days
                #else, uses the default expiry at browser close

                return HttpResponseRedirect(redirect)
            else:
                login_form.add_error(None, 'Those are invalid credentials. Please try again.')
    else:
        login_form = forms.LoginForm()

    return render(request, 'bithumb/index.html', {'signup_form': signup_form, 'login_form': login_form})


def profile(request, user_id=None):
    if user_id == None and request.user.is_authenticated:
        user_id = request.user.pk

    user = get_object_or_404(models.User, pk=user_id)

    return render(request, 'account/profile.html', {'user': user})

def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))
