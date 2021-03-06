# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2018-03-11 20:43
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('invest', '0002_auto_20180311_1443'),
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='id',
        ),
        migrations.AddField(
            model_name='user',
            name='_bank_account',
            field=models.OneToOneField(default=1, on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='invest.BankAccount'),
        ),
        migrations.AddField(
            model_name='user',
            name='highscore',
            field=models.DecimalField(decimal_places=0, default=0, max_digits=20),
        ),
    ]
