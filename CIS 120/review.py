"""Victoria Braden
CIS120 """

#Flyer Program

"""bagWeight = 0
bagWeight = int(raw_input("How much does your bag weigh? "))

if (bagWeight > 50):
    print "There will be an extra $25 fee."
print "Thank you for your business."    
"""

#get weather temperature
#if temp above 70 wear shorts
#or wear long pants
#get some excersize outside

"""temp = 0
temp = int(raw_input("What is the temperature fo the day? "))

if (temp > 70):
    print "Wear some shorts!"
else:
    print "Wear some long pants!"
print "Now go get some excersize outside!"
"""

#ask for number
#print if pos neg or zero

"""num = 0
num = int(raw_input("Please insert a number. "))

print "Your number is",
if (num > 0):
    print "positive."
elif (num == 0):
    print "0."
else:
    print "negative."
"""

#calculate GPA
#get all test scores and give total GPA

"""cGPA = 0.0
testScore = 0.0
keepGoing = "y"
count = 0
while keepGoing == "y":
    testScore = int(raw_input("Enter a test score: "))
    cGPA += testScore
    count += 1
    keepGoing = raw_input("Add another test score? (y/n) ")

cGPA = cGPA/count

#print "The cummulative GPA is " + str(cGPA)
print ("The cummulative GPA is %.2f" % cGPA)
"""

#Standard for loop
#for (i = 0 ; i < 5 ; i ++)

#python for loop
#for x in range (3,8,2)
#(starting point, how many places to go, increment)

#bug colector collects bugs every day for 7 days
#running total of how many bugs each day
#end display total number of bugs

bugs = 0
bugTotal = 0
for x in range(1,8):
    bugs = int(raw_input("How many bugs were caught today? "))
    bugTotal += bugs
    print ("Bugs for day %x are %i" % (x, bugs))

print ("The total number of bugs collected is %i" % bugTotal)
