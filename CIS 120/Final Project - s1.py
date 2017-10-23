bookAry = [["Heylin Restart", "Vicky & Kayla Rose", 19.95],
           ["101 Ways to Romance a Mythical Being", "Chase Young", 5.00],
           ["How To Tell If Your Child Is Actually A Dragon", "WeirdWyvern", 14.50]]          
gameAry = [["Spicer Academy", "Vicky & Kayla Rose", 14.99],
           ["Bad Decision of the Day", "Jack Spicer", 199.95],
           ["Cooking Time with Hannibal Roy Bean", "WeirdWyvern", 9.95]]
start = 0
purchase = []
bookBuy = -1
gameBuy = -1
done = "y"
subTotal = 0

print "Welcome to Froggy's Books and Games!"

while done == "y":
    while start != "1" and start != "2":
        start = str(raw_input("What would you like to do today?\n"\
                          "1 - Purchase Books\n"\
                          "2 - Purchase Games\n"))
    #books
    if start == "1":
        print "You've selected Books. Which book will be purchased?\n"
        for i in range (len(bookAry)):
            print "ID:%i - %s by %s - $%.2f\n" % (i, bookAry[i][0], bookAry[i][1], bookAry[i][2])

        while bookBuy not in range (len(bookAry)):
            bookBuy = int(raw_input("Enter Book ID: "))
        print "You've selected: %s" % bookAry[bookBuy][0]
        ammount = int(raw_input("How many copies?\n"))
        purchase.append([bookAry[bookBuy][0],bookAry[bookBuy][1],
                         bookAry[bookBuy][2],ammount])
        print purchase
        done = str(raw_input("Add another Item?\n")).lower()
        bookBuy = -1
        start = 0
        
    #games 
    elif start == "2":
        print "You've selected Gamess. Which game will be purchased?\n"
        for i in range (len(gameAry)):
            print "ID:%i - %s by %s - $%.2f\n" % (i, gameAry[i][0], gameAry[i][1],gameAry[i][2])

        
        while gameBuy not in range (len(gameAry)):
            gameBuy = int(raw_input("Enter Game ID: "))
        print "You've selected: %s" % gameAry[gameBuy][0]
        ammount = int(raw_input("How many copies?\n"))
        purchase.append([gameAry[gameBuy][0],gameAry[gameBuy][1],
                         gameAry[gameBuy][2],ammount])
        done = str(raw_input("Add another Item?\n")).lower()
        gameBuy = -1
        start = 0

for x in range (len(purchase)):
    subTotal += (purchase[x][2] * purchase[x][3])
print "\nYou've purchased: \n"
for y in range (len(purchase)):
    print "%i - %s by %s - $%.2f each\n" % (purchase[y][3],purchase[y][0],purchase[y][1],purchase[y][2])
print "Purchase Total: $%.2f\n" % subTotal
tax = subTotal * .08
total = subTotal + tax
print "Tax: $%.2f\n" % (tax)
print "Total Purchase: $%.2f" % (total)
print "\nThank you, come again!"
