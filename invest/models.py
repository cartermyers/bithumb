# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

from decimal import Decimal

class BankAccount(models.Model):
    #see https://en.bitcoin.it/wiki/Units
    #min value is 1 satoshi (8 decimal places)
    #and max value is 1,000,000 bitcoins (hence 15 total digits)
    bitcoins = models.DecimalField(max_digits=15, decimal_places=8, default=0)

    #actual in game currency (analagous to CAD, hence 2 decimal places)
    #and we'll say max 999,999,999,999,999 (so 17 total digits)
    in_game_currency = models.DecimalField(max_digits=17, decimal_places=2, default=0)

    #NOTE: since the rate will be pushed real time to the user,
    #we we can assume the rate can be passed
    def exchange_bitcoin_for_in_game_currency(self, bitcoin, rate):
        if bitcoin > self.bitcoins:
            raise AssertionError

        self.bitcoins -= Decimal(str(bitcoin))
        self.in_game_currency += Decimal(str(bitcoin * rate))
        self.save()

    def exchange_in_game_currency_for_bitcoin(self, in_game_currency, rate):
        if in_game_currency > self.in_game_currency:
            raise AssertionError

        self.in_game_currency -= Decimal(str(in_game_currency))
        self.bitcoins += Decimal(str(in_game_currency / rate))
        self.save()

    def deposit_in_game_currency(self, new_amount):
        self.user.set_highscore(new_amount)
        self.user.save()
        self.in_game_currency += Decimal(str(new_amount))

    def get_bitcoins(self):
        return float(self.bitcoins)

    def get_in_game_currency(self):
        return float(self.in_game_currency)

    #TODO: setters
    #also convert (private), and withdraw and deposit (both for investments) OR do these belong as views?

#these are in-game Collectibles that users can purchase
#with in-game currency
#This class is only edited by devs
class Collectible(models.Model):

    #we might change the max later
    price = models.DecimalField(max_digits=17, decimal_places=2)
    name = models.CharField(max_length=127)
    image = models.ImageField(upload_to='collectibles/')

    def get_name(self):
        return self.name

    def get_price(self):
        return float(self.price)

    def get_image(self):
        return self.image.url

    #This should need no setters as this is added directly to the DB by devs (static objects)

    def __str__(self):
        return self.name



#here's another model to keep track of the many-to-many relationship
#between accounts and collectibles (that is, one account can own many collectibles
#and the same collectible can be owned by many accounts)
class BankAccountToCollectible(models.Model):
    account = models.ForeignKey(BankAccount, on_delete=models.CASCADE)
    collectible = models.ForeignKey(Collectible, on_delete=models.CASCADE)

    #TODO: setters and getters
