#victoria Braden
#CIS 120
#slot Machine

from random import *

fruits = ["Cherries","Oranges","Plums","Bells","Melons","Bars"]
playCash = 100
arySlots = []
bet = 0
playMore = "y"

def placeBet():
    global bet
    bet = int(raw_input("How much would you like to bet?"))
    if bet > playCash:
        print ("Sorry, you dont have enough cash to bet that ammount!")
        placeBet()
    

while playMore == "y":
    if playCash > 0:
        print ("Let's play! Your current cash ammount is %i!") % (playCash)
        placeBet()
    
        for i in range(3):
            numb = randint(0,5)
            arySlots.append(numb)
            print fruits[numb]

        if arySlots[0] == arySlots[1]:
            if arySlots[1] == arySlots[2]:
                playCash = playCash + 75
                print ("Yay! You won 75!")
                arySlots = []
            else:
                playCash = playCash + 25
                print ("Yay! You won 25!")
                arySlots = []
        elif arySlots[1] == arySlots[2]:
            playCash = playCash + 25
            print ("Yay! You won 25!")
            arySlots = []
        else:
            playCash = playCash - bet
            print ("Nothin' doing!")
            arySlots = []
        playMore = str(raw_input("Want to play again? (y/n) ").lower())
    else:
        print "Sorry you're out of cash! Game over!"
        playMore = "n"

print ("See ya next time!")
