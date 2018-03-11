# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

from account.models import User

class Forum(models.Model):
    poster = models.ForeignKey(User, on_delete=models.CASCADE)

    # own attributes
    title = models.CharField(max_length=255)
    description = models.TextField(null=True)   #this is the main body of the post
    time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    #TODO: setters and getters
    #also observer methods

class Comments(models.Model):
    post = models.ForeignKey(Forum, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    text = models.CharField(max_length=500)
    time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.text

    #TODO: setters and getters

    #also observer methods? maybe a mixin?
