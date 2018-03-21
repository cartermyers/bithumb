# this is a script to be run from the django shell
# used to populate the database with collectibles
# THIS SHOULD ONLY BE RUN ONCE (and if the table is empty)
# this is simply used to easily add/modify all collectibles

if __name__ == "__main__":
    from invest.models import Collectible
    from decimal import Decimal
    from sys import exit

    if len(Collectible.objects.all()) > 0:
        print "Collectibles table not empty. Exiting script."
        exit()

    #else create all the collectibles
    bronze = Collectible(price=Decimal('100'), name='Bronze trophy', image='static/img/collectibles/bronze.png')
    silver = Collectible(price=Decimal('1000'), name='Silver trophy', image='static/img/collectibles/silver.png')
    gold = Collectible(price=Decimal('10000'), name='Gold trophy', image='static/img/collectibles/gold.png')
    bitcoin = Collectible(price=Decimal('100000'), name='Bitcoin trophy', image='static/img/collectibles/bitcoin.png')

    #and save them all:
    bronze.save()
    silver.save()
    gold.save()
    bitcoin.save()

    print "Successfully created all trophies"
