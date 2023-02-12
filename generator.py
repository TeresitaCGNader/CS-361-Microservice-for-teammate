#You DO NOT need to use this code
#This is the piece of code that was implemented in the client and server
#to randomly generate a card name from the text file "card_list.txt"
#This code opens the file, reads the file and prints a random string variable (e.g. lines)

import random
def random_line(fname):
    lines = open(fname).read().splitlines()
    return random.choice(lines)

printme = random_line('card_list.txt')

print(printme)
