# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2018-03-11 21:12
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('invest', '0002_auto_20180311_1443'),
    ]

    operations = [
        migrations.RenameField(
            model_name='bankaccount',
            old_name='bitcoins',
            new_name='_bitcoins',
        ),
        migrations.RenameField(
            model_name='bankaccount',
            old_name='in_game_currency',
            new_name='_in_game_currency',
        ),
    ]
