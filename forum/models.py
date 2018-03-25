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

    def set_poster(self, user):
        self.poster = user
        self.save()

    def set_description(self, text):
        self.description = text
        self.save()

    def set_title(self, new_title):
        self.title = new_title
        self.save()

    def get_title(self):
        return self.title

    def get_description(self):
        return self.description

    def get_time(self):
        return self.time

    def get_poster(self):
        return self.poster

class Comments(models.Model):
    post = models.ForeignKey(Forum, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    text = models.CharField(max_length=500)
    time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.text

    def set_user(self, new_user):
        self.user = new_user

    def set_post(self, new_post):
        self.post = new_post
    #TODO: setters and getters
