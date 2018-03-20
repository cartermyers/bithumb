#here is a script to run permanently on the server to push updates to users for bitcoin prices

#here is some code taken from https://help.pythonanywhere.com/pages/LongRunningTasks/
# to ensure code only runs when it's supposed to
import socket
import sys

lock_socket = None  # we want to keep the socket open until the very end of
                    # our script so we use a global variable to avoid going
                    # out of scope and being garbage-collected

def is_lock_free():
    global lock_socket
    lock_socket = socket.socket(socket.AF_UNIX, socket.SOCK_DGRAM)
    try:
        lock_id = "shin202j.update_price"   # this should be unique. using your username as a prefix is a convention
        lock_socket.bind('\0' + lock_id)
        return True
    except socket.error:
        return False

if not is_lock_free():
    sys.exit()

#here are all of the update functions:
from bitcoin_price_api.update_price import update_price

#this function has a while loop that should run forever
update_price()
