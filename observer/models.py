# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.conf import settings
from django.views import View

from pusher import Pusher

#abstract classes for observer model
#this is slightly modified because we use the Pusher app
#some code is taken from https://github.com/pusher/django-pusherable in the mixins.py and templatetags.py

class Observer(View):

    def __init__(self):
        _subject = None  #each class will keep track of its subject

    def get_subject(self):
        return self._subject

    def set_subject(self, subject):
        self._subject = subject

    @staticmethod
    def pusherable_script():
        return "<script src=\"//js.pusher.com/2.2/pusher.min.js\" type=\"text/javascript\"></script>"

    @staticmethod
    def update(subject):
        event = 'update'
        channel = 'presence-' + type(subject).__name__

        try:
            channel += "_" + subject.pk
        except AttributeError:
            pass

        return """
        <script type=\"text/javascript\">
        var pusher = new Pusher('{key}', {{cluster: '{cluster}'}});
        var channel = pusher.subscribe('{channel}');
        channel.bind('{event}', function(data) {{
          pusherable_notify('{event}', data);
        }});
        </script>
        """.format(
            key=settings.PUSHER_KEY,
            cluster=settings.PUSHER_CLUSTER,
            channel=channel,
            event=event)

class Subject(object):

    #interface that is implemented by child
    #must return a dict
    def get_state(self):
        return {}

    def channel(self):
        #this is the channel on pusher that we will broadcast on
        #similar to the observer list in the traditional pattern
        channel = 'presence-' + type(self).__name__
        try:
            channel += "_" + self.pk
        except AttributeError:
            pass

        return channel

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

        #first, see if there are any users (if not, don't bother notifying)
        if not pusher.channel_info(self.channel(), ['user_count'])['occupied']:
            return

        pusher.trigger(
            [self.channel(), ],
            "update",
            {
                'object': self.get_state(), #implemented in child class
            }
        )
