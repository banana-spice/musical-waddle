def hello():
    print "We are the Warner Bros & the Warner Sister"
def timesFour(charName, numHellos):
    saysHello = ("o" * numHellos)
    print charName, "says Hell" + saysHello + " Nurse!"

class Critter():
    def talk(self,critterName):
        print "HI! I'M AN INSTANCE OF CRITTER!"
        self.name = critterName
