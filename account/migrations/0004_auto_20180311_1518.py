# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2018-03-11 21:18
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0003_auto_20180311_1443'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='highscore',
            new_name='_highscore',
        ),
    ]
