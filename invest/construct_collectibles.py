# this is a script to be run from the django shell
# used to populate the database with collectibles
# THIS SHOULD ONLY BE RUN ONCE (and if the table is empty)
# this is simply used to easily add/modify all collectibles

from invest.models import CollectibleBuilder, Collectible
from decimal import Decimal

class CollectibleConstructor:

    @staticmethod
    def build_all():
        CollectibleConstructor.build_bronze()
        CollectibleConstructor.build_silver()
        CollectibleConstructor.build_gold()
        CollectibleConstructor.build_bitcoin()

    @staticmethod
    def build_bronze():
        builder = CollectibleBuilder()
        builder.set_name("Bronze trophy")
        builder.set_price(Decimal('100'))
        builder.set_image('collectibles/bronze.png')
        builder.save()

    @staticmethod
    def build_silver():
        builder = CollectibleBuilder()
        builder.set_name("Silver trophy")
        builder.set_price(Decimal('1000'))
        builder.set_image('collectibles/silver.png')
        builder.save()

    @staticmethod
    def build_gold():
        builder = CollectibleBuilder()
        builder.set_name("Gold trophy")
        builder.set_price(Decimal('10000'))
        builder.set_image('collectibles/gold.png')
        builder.save()

    @staticmethod
    def build_bitcoin():
        builder = CollectibleBuilder()
        builder.set_name("Bitcoin trophy")
        builder.set_price(Decimal('100000'))
        builder.set_image('collectibles/bitcoin.png')
        builder.save()

#if its executed within the django shell:
if __name__ == "__builtin__":
    from sys import exit

    if len(Collectible.objects.all()) > 0:
        print "Collectibles table not empty. Exiting script."
    else:
        #and construct them all:
        CollectibleConstructor.build_all()
        print "Successfully created all trophies"
