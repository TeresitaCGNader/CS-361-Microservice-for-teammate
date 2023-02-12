#
#   Random Card Name generator server in Python
#   Binds REP socket to tcp://*:5555
#   Expects printme variable from client, replies with Random Card Name
#

import time
import zmq
import random

def random_line(fname):
    lines = open(fname).read().splitlines()
    return random.choice(lines)
printme = random_line('card_list.txt')

context = zmq.Context()
socket = context.socket(zmq.REP)
socket.bind("tcp://*:5555")

while True:
    #  Wait for next request from client
    message = socket.recv()
    print(f"Received request: {message}")

    #  Do some 'work'
    time.sleep(1)

    #  Send reply back to client
    socket.send_string(printme)
