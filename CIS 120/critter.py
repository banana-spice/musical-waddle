class Critter():
    def __init__(self, critterName):
        self.name = critterName
    def talk(self):
        print "HI!", self.name
    def hello(self, numb):
        saysHello = ("o" * numb)
        print self.name, "says Hell" + saysHello + " Nurse!"

crit = Critter("Wakko")
crit.talk()
print crit.name
crit.hello(5)

crit2 = Critter("Yakko")
crit2.talk()
print crit2.name
crit2.hello(8)

crit3 = Critter("Dot")
crit3.talk()
print crit3.name
crit3.hello(1)
