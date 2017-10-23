#create the array of books to be filled from the file
aryBooks=[] 
cumPrice = 0

#open the text file stream for reading
books = open("FroggyBooks.txt", "r") 

#read the lines from the text file
lines=books.readlines() 

#loop through each line
for line in lines: 
    #split the lines apart at each comma
    #and append each piece into the array
    aryBooks.append(line.split(","))    
    print line
    
for i in range (len(aryBooks)):
      #convert the price to a float
      cumPrice += float(aryBooks[i][2])
print cumPrice, " total"
    

