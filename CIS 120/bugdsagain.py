#bug collector

"""
totbugs = 0
keepgoing = "Y"

def addbugs():
    global totbugs
    subbugs = int(raw_input("bugs: "))
    totbugs += subbugs

while keepgoing == "Y":
    addbugs()
    keepgoing = raw_input("More bugs? ").upper()
    
print ("total bugs: %i" % totbugs)
"""
#bug collector return variable


totbugs = 0
keepgoing = "Y"

def addbugs():
    subbugs = int(raw_input("bugs: "))
    return subbugs

while keepgoing == "Y":
    tmpbugs = addbugs()
    totbugs += tmpbugs
    keepgoing = raw_input("More bugs? ").upper()
    
print ("total bugs: %i" % totbugs)


