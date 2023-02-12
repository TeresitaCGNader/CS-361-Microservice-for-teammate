#
#   Random Card Name generator client in Python
#   Connects REQ socket to tcp://localhost:5555
#   Sends printme variable to server
#

import zmq
import random

context = zmq.Context()


def random_line(fname):
    lines = open(fname).read().splitlines()
    return random.choice(lines)
printme = random_line('card_list.txt')
    
#  Socket to talk to server
print("Connecting to server…")
socket = context.socket(zmq.REQ)
socket.connect("tcp://localhost:5555")

#  Do 1 request, waiting each time for a response
for request in range(1):
    print(f"Sending request {request} …")
    socket.send_string(printme)

    #  Get the reply.
    message = socket.recv()
    print(f"Received reply {request} [ {message} ]")
