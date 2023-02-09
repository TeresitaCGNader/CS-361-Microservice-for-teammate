#
#   Hello World client in Python
#   Connects REQ socket to tcp://localhost:5555
#   Sends "Hello" to server, expects "World" back
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

#  Do 10 requests, waiting each time for a response
#for request in range(10):
for request in range(1):
    print(f"Sending request {request} …")
    #socket.send(b"Hello")
    #socket.send(b"A message from CS361")
    socket.send_string(printme)

    #  Get the reply.
    message = socket.recv()
    print(f"Received reply {request} [ {message} ]")