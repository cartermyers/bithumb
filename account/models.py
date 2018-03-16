# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import AbstractUser

from invest.models import BankAccount

class User(AbstractUser):
    """ See https://docs.djangoproject.com/en/2.0/ref/contrib/auth/#django.contrib.auth.models.User
        for all inherited attributes and methods (AbstractUser is the same as User).
        Any fields that we are using should be in accounts.forms under SignupForm"""

    #a game highscore (to be changed later based on implementation)
    highscore = models.DecimalField(max_digits=20, decimal_places=0, default=0)
    bank_account = models.OneToOneField(BankAccount, on_delete=models.DO_NOTHING, primary_key=True)

    def save(self, *args, **kwargs):
        #we also need to create a corresponding bank account for each new user
        # (new users will not have a bank account id)
        if not self.bank_account_id:
            self.bank_account = BankAccount.objects.get_or_create(pk=self.pk)[0]

        super(AbstractUser, self).save(*args, **kwargs)

    def delete(self, *args, **kwargs):
        #and delete the BankAccount too
        # (just except any errors for robustness)
        try:
            BankAccount.objects.get(pk=self.bank_account_id).delete()
        except BankAccount.DoesNotExist:
            pass

        super(AbstractUser, self).delete(*args, **kwargs)

    #setters
    def set_password(self, new_pass):
        self.password = new_pass

    def set_highscore(self, new_high):
        self.highscore = new_high

    #getters
    def get_highscore(self):
        return self.highscore

    def get_bank_account(self):
        return BankAccount.objects.get(pk=self.bank_account_id)




class Admin(User):
    """ Admins have all the same functionality as regular users, but with some extra functionalities """
    pass

    #TODO: setters and getters
