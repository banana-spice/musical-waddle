#victoria Braden
#CIS 120
#ro sham bo

from random import *
playAgain = "Y"
num = 0
playNum = 0
playWins = 0
compWins = 0

def doitthisway():
    global playNum
    playNum = int(raw_input("Pick your poison! Put 1 for Rock, "\
                            "2 for Paper, or 3 for Scissors: "))
    print playNum
    if playNum == 1:
        playnow = "Rock"
        return playnow
    elif playNum == 2:
        playnow = "Paper"
        return playnow
    elif playNum == 3:
        playnow = "Scissors"
        return playnow
    else:
        print ("Please enter 1, 2, or 3.")
        playnow = doitthisway()
        return playnow

print "Let's play!"
while playAgain == "Y":

    num = randint(1,3)
    if num == 1:
        comTry = "Rock"
    elif num == 2:
        comTry = "Paper"
    else:
        comTry = "Scissors"

    playTry = doitthisway()
        
    print "%s VS %s!" % (comTry, playTry)
    
    if num == playNum:
        print "Oops! It's a tie! No winners."
    elif (num == 1) and (playNum == 3):
        print "Computer wins!"
        compWins += 1
    elif (num == 1) and (playNum == 2):
        print "You win!"
        playWins += 1
    elif (num == 2) and (playNum == 1):
        print "Computer wins!"
        compWins += 1
    elif (num == 2) and (playNum == 3):
        print "You win!"
        playWins += 1
    elif (num == 3) and (playNum == 1):
        print "You win!"
        playWins += 1
    elif (num == 3) and (playNum == 2):
        print "Computer wins!"
        compWins += 1

    playAgain = raw_input("Would you like to play again? (Y/N) ").upper()
    num = 0

if compWins > playWins:
    print "Ooh Sory! Better luck next time!"
elif compWins == playWins:
    print "Well look at that! You tied!"
else:
    print "Congrats! You're a Ro Sham Bo Champ!"

print "Wins: %i Losses: %i" % (playWins,compWins)
