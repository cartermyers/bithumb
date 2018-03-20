#here is the actual script to update the price
import time
from .exchanges import CoinDesk

def update_price():
    subject = CoinDesk()

    #use a variable to see if the state has changed and we need to push to the client
    old_state = subject.get_state()['price']

    while True:
        new_price = subject.get_state()['price']
        if new_price != old_state:
            old_state = new_price
            subject.notify()

        #only check about every 5 seconds
        time.sleep(5)