import random

compScore = 0
playScore = 0
compSel = -1
playSel = -1
suit = ["Spades","Hearts","Diamonds","Clubs"]
card = ["1","2","3","4","5","6","7","8","9","10","Jack","Queen","King","Ace"]
letsPlay = "Y"
tied = "y"

while letsPlay == "Y":
    while compSel == playSel:
        compSel = random.randint(0,13)
        playSel = random.randint(0,13)
        cSuit = random.randint(0,3)
        pSuit = random.randint(0,3)
        print "\nComputer's Card: %s of %s\n" % (card[compSel],suit[cSuit])
        print "Player's Card: %s of %s\n" % (card[playSel],suit[pSuit])
        if compSel > playSel:
            print "Computer Wins!"
            compScore += 1
        elif compSel < playSel:
            print "Player Wins!"
            playScore += 1
        else:
            print "Tied!"
            

    print ("Computer: %i     Player: %i") % (compScore,playScore)
    compSel = -1
    playSel = -1
    letsPlay = str(raw_input("Do you want to play again? (press Y to continue) ")).upper()

print ("\nThe final score is:\nComputer: %i   Player %i") % (compScore,playScore)
if compScore > playScore:
    print "The Computer is the winner!"
elif compScore < playScore:
    print "The Player is the winner!"
elif compScore == playScore:
    print "It's a tie!"

print "Thanks for playing!"
    
    
