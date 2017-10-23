scores = []
choice = None

print "Welcome to the game of highscores\n"
print "Select 0 to end the game\n"
print "Select 1 to enter scores\n"
print "Select 2 to sort scores\n"
print "Select 3 to delete a score\n"


while choice != "0":
    choice = raw_input("What shall we do? ")
    if choice == "0":
        scores.sort()
        scores.reverse()
        highScore = scores.pop(0)
        print "High Score:", highScore
        print "goodbye"
    elif choice == "1":
        score = int(raw_input("What score did you get? "))
        scores.append(score)
    elif choice == "2":
        scores.sort()
        scores.reverse()
    elif choice == "3":
        score = int(raw_input("Which score is removed? "))
        if score in scores:
            scores.remove(score)
        else:
            print score, "isn't in the list"


    print scores
