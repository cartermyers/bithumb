# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    """ See https://docs.djangoproject.com/en/2.0/ref/contrib/auth/#django.contrib.auth.models.User
        for all inherited attributes and methods (AbstractUser is the same as User).
        Any fields that we are using should be in accounts.forms under UserForm"""
    pass

    #TODO: setters and getters




class Admin(User):
    """ Admins have all the same functionality as regular users, but with some extra functionalities """
    pass

    #TODO: setters and getters
