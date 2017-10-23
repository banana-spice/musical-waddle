'''
#define module
def hello():
    print "Hello!"

hello()#call the module
'''

'''
#sending an argument to a parameter
def hello(whatToPrint): #parameter is the variable
    print whatToPrint #makes it print the valuereceived in the parameter

hello("sending a value") #sends arguement to module
print "last line to print"
'''

'''
def hello(name, greeting, age):
    print "Hello " + name + " " + greeting + "! You are %i" % age + " today."

usrName = raw_input("What is your name? ")
usrAge = int(raw_input("How old are you? (Please enter a whole number) "))
hello(usrName, "Good morning", usrAge)

print "good bye"
'''

'''
count = 6 #global variables - available to whole program
def forloopReview():
    #count = 6
    #variables in functions are local to the function
    #only said function has access
    for x in range(1, count):
        print x

forloopReview()
print count
'''

'''
def validate(strToPrint):
    strToPrint = strToPrint.upper()

    if strToPrint == "Y":
        print "Yes was entered"
    elif strToPrint == "N":
        print "No was entered"
    else:
        print "Something else was entered"
        keepGoing = raw_input("Still want to play? (Y/N) ")
        validate(keepGoing)
keepGoing = raw_input("Still want to play? (Y/N) ")
validate(keepGoing)
'''

#Bug Collector
totBugs = 0
keepGoing = "Y"

def addBugs():
    global totBugs
    subBugs = int(raw_input("Bugs: "))
    totBugs += subBugs

while keepGoing == "Y":
    addBugs()
    keepGoing = raw_input("Anymore bugs to add? (Y/N)").upper()

print ("Total Bugs: %i" % totBugs)
