# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2018-03-11 21:28
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0004_auto_20180311_1518'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='_bank_account',
            field=models.OneToOneField(on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, serialize=False, to='invest.BankAccount'),
        ),
    ]
