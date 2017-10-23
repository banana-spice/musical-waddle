bookAry = []
gameAry = []

books = open("froggybooks.txt", "r") 

lines=books.readlines() 

for line in lines: 
    bookAry.append(line.split(","))    

games = open("froggygames.txt", "r") 

lines=games.readlines() 

for line in lines: 
    gameAry.append(line.split(","))    


start = 0
purchase = []
bookBuy = -1
gameBuy = -1
done = "y"
subTotal = 0

print "Welcome to Froggy's Books and Games!"

while start != "1" and start != "2":
    start = str(raw_input("What would you like to do today?\n"\
                          "1 - Purchase Books\n"\
                          "2 - Purchase Games\n"))
#books
if start == "1":
    print "You've selected Books. Which book will be purchased?\n"
    for i in range (len(bookAry)):
        print "ID:%i - %s by %s - $%0.2f\n" % (i, bookAry[i][0], bookAry[i][1], bookAry[i][2])

    while done == "y":
        while bookBuy not in range (len(bookAry)):
            bookBuy = int(raw_input("Enter Book ID: "))
        print "You've selected: %s" % bookAry[bookBuy][0]
        purchase.append(bookAry[bookBuy])
        done = str(raw_input("Add another Item?\n")).lower()
        bookBuy = -1
        
#games 
elif start == "2":
    print "You've selected Gamess. Which game will be purchased?\n"
    for i in range (len(gameAry)):
        print "ID:%i - %s by %s - $%0.2f\n" % (i, gameAry[i][0], gameAry[i][1],gameAry[i][2])

    while done == "y":
        while gameBuy not in range (len(gameAry)):
            gameBuy = int(raw_input("Enter Game ID: "))
        print "You've selected: %s" % gameAry[gameBuy][0]
        purchase.append(gameAry[gameBuy])
        done = str(raw_input("Add another Item?\n")).lower()
        gameBuy = -1
        

for x in range (len(purchase)):
    subTotal += purchase[x][2]
print "\nYou've purchased: \n"
for y in range (len(purchase)):
    print "%s by %s - $%0.2f\n" % (purchase[y][0],purchase[y][1],purchase[y][2])
print "Purchase Total: $%0.2f\n" % subTotal
tax = subTotal * .08
total = subTotal + tax
print "Tax: $%0.2f\n" % (tax)
print "Total Purchase: $%0.2f" % (total)
print "\nThank you, come again!"
