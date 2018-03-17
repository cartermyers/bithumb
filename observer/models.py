# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.conf import settings
from django import template

from pusher import Pusher

#abstract classes for observer model
#this is slightly modified because we use the Pusher app
#some code is taken from https://github.com/pusher/django-pusherable in the mixins.py and templatetags.py

register = template.Library()

class Observer(object):

    @register.simple_tag
    def pusherable_script():
        return "<script src=\"//js.pusher.com/2.2/pusher.min.js\" type=\"text/javascript\"></script>"

    @register.simple_tag
    def update(event, subject):
        channel = type(subject).__name__

        try:
            channel += "_" + subject.pk
        except AttributeError:
            pass

        return """
        <script type=\"text/javascript\">
        var pusher = new Pusher('{key}', {cluster: '{cluster}'});
        var channel = pusher.subscribe('{channel}');
        channel.bind('{event}', function(data) {{
          pusherable_notify('{event}', data);
        }});
        </script>
        """.format(
            key=settings.PUSHER_KEY,
            cluster=settiings.PUSHER_CLUSTER,
            channel=channel,
            event=event
        )

class Subject(object):
    #this is the channel on pusher that we will broadcast on
    #similar to the observer list in the traditional pattern
    def channel(self):

        channel = type(self).__name__
        try:
            channel += "_" + subject.pk
        except AttributeError:
            pass

        return channel

    def get_state(self):
        pass

    #this is the notify function with a push method
    def notify(self):
        try:
            pusher_cluster = settings.PUSHER_CLUSTER
        except AttributeError:
            pusher_cluster = 'mt1'

        pusher = Pusher(app_id=settings.PUSHER_APP_ID,
                        key=settings.PUSHER_KEY,
                        secret=settings.PUSHER_SECRET,
                        cluster=pusher_cluster)

        pusher.trigger(
            [self.channel(), ],
            "update",
            {
                'object': self.get_state(), #implemented in child class
            }
        )
