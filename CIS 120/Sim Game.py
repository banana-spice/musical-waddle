import sys
import time

#abilities
strMod = 0
chaMod = 0
intMod = 0
magicMod = 0

troubleSkill = 0
inClass = "n"

#class skills
musicSkill = 0
artSkill = 0
scienceSkill = 0
culinarySkill = 0

#sciences
robotSkill = 0
bioChemSkill = 0
astroSkill = 0
programSkill = 0
botanySkill = 0

#available jacks
jackNam = ["Hot Dad","Jianyu","Animack","Bat","Specter",\
           "Gack","Marshmallow","Moon","Void"]
jack = [0,0,0,0,0,\
        0,0,0,0]

def genderPick():
    gend = str(raw_input("Are you a boy or a girl? (b/g)").lower())
    if gend == "b":
        gend = "Boy"
    elif gend == "g":
        gend = "Girl"
    else:
        print ("Sorry, didn't get that. Try again.")
        gend = genderPick()
    return gend

def slow_print(str):
    for letter in str:
        sys.stdout.write(letter)
        sys.stdout.flush()
        time.sleep(0.01)

def print_totals():
    print ("Abilities:")
    print ("Int: %i, Str: %i, Cha: %i, Magic: %i")\
          % (intMod,strMod,chaMod,magicMod)
    if inClass == "y":
        print ("Class Skills:")
        print ("Music: %i, Art: %i, Culinary: %i, Science: %i")\
          % (musicSkill,artSkill,culinarySkill,scienceSkill)
    if scienceSkill > 0:
        print ("Sciene Skills:")
        print ("Robotics: %i, BioChemistry: %i, Astro Science: %i, "\
           "Programming: %i, Botany: %i")\
           % (robotSkill,bioChemSkill,astroSkill,programSkill,botanySkill)
    print ("Trouble Level: %i") % (troubleSkill)

def question1A():
    global intMod
    global troubleSkill
    global strMod
    que1A = str(raw_input("A: Yes, Quick! Hurry! Bears are scary... "\
                          "B: I guess I'll go, then. "\
                          "C: Siiiigh, Fffiiiine... "\
                          "D: I'll risk it with the bears.").upper())
    if que1A == "A":
        intMod = intMod + 5
        reply = "y"
        return reply
    elif que1A == "B":
        intMod = intMod + 2
        strMod = strMod + 2
        reply = "y"
        return reply
    elif que1A == "C":
        troubleSkill = troubleSkill + 3
        reply = "y"
        return reply
    elif que1A == "D":
        strMod = strMod + 1
        troubleSkill = troubleSkill + 5
        reply = "n"
        return reply
    else:
        print ("Please select A, B, C or D.")
        reply = question1A()
        return reply

def gowithtoschool():
    global intMod
    global chaMod
    global troubleSkill
    gotoschool = str(raw_input("Will you go with them? (y/n) ").lower())
    if gotoschool == "n":
        intMod = intMod + 1
        print (" ")
        slow_print ("Animack: Seriously? You'd rather stay out here? "\
                    "You know there are BEARS right? Pretty damn big ones too..."\
                    " *His eyes darted around suspiciously in sudden paranoia*")
        print (" ")
        print (" ")
        slow_print ("Bat: *Bat began laughing at Animack's outburst* "\
                    "If anyone would know about that, it'd definitely"\
                    " be you, bike boy.")
        print (" ")
        print (" ")
        slow_print ("Animack: Hey, fuck you! *Bat's laughter "\
                    "increased ten-fold at the outburst. Animack "\
                    "gave a literal and animalistic growl at his companion* ")
        print (" ")
        print (" ")
        slow_print ("*You take a step backward away from Animack. He notices "\
                    "a split second later and stops growling.*")
        print (" ")
        print (" ")
        slow_print ("Animack: Er... sorry. Heh, sometimes I can't help myself."\
                    " *He rubbed the back of his neck obviously embarrassed.* "\
                    "Anyway, we should go.")
        print (" ")
        print (" ")
        gotoschool = question1A()
        return gotoschool
        
    elif gotoschool == "y":
        chaMod = chaMod + 2
        return gotoschool
    else:
        print ("Please input y or n.")
        gotoschool = gowithtoschool()
        return gotoschool

def askaboutbat():
    global chaMod
    global troubleSkill
    global jack
    whatudo = str(raw_input("A: What the fuck are you doing? "\
                            "B: Is that something important?").upper())
    if whatudo == "A":
        troubleSkill = troubleSkill + 2
        jack[2] = jack[2] + 2
        jack[3] = jack[3] - 1
        print (" ")
        slow_print ("Bat: *This time it was Animack who started laughing. "\
                    "Bat gave a large pout and crossed his arms.* "\
                    "I'm collecting spices. *His flat statement being all the "\
                    "explanation he intended to give you.*")
    elif whatudo == "B":
        chaMod = chaMod + 2
        jack[3] = jack[3] + 2
        print (" ")
        slow_print ("Animack: Oh don't get him started... *Animack grumbled "\
                    "but it was clearly too late. Bat's eyes lit up with "\
                    "full hearted excitement.*")
        print (" ")
        print (" ")
        slow_print("Bat: I'm collecting spices and other useful stuff "\
                   "that grows here. *He told you as he fished out a few "\
                   "of the plant bits and shiny bobbles he'd collected "\
                   "already. You smile at his odd treasures before he quickly "\
                   "stashes them away again.*")

def askhimnow():
    global intMod
    askinghim = str(raw_input("Ask Bat what he's doing? (y/n) ").lower())
    if askinghim == "y":
        askaboutbat()
    elif askinghim == "n":
        intMod = intMod + 1
    else:
        print ("Please input y or n.")
        askinghim = askhimnow()

def ontheotherhand():
    global troubleSkill
    global intMod
    nevermind = str(raw_input("A: Uhhh Hey guys, I changed my mind! *Go after Bat"\
                              "and Animack, they're still in sight!*  "\
                              "B: Pff, bears. I'm not scared of any bear! "\
                              "*Continue on this path towards possibly doom.*").upper())
    if nevermind == "A":
        intMod = intMod + 3
        nevermind = "y"
        return nevermind
    elif nevermind == "B":
        troubleSkill = troubleSkill + 5
        nevermind = "n"
        return nevermind
    else:
        print ("Please enter A or B.")
        nevermind = ontheotherhand()
        return nevermind
                        
#game start
gender = genderPick()

print (" ")
print (" ")
slow_print ("Fresh outta high school and ready for college... ")
print (" ")
slow_print ("What's a %s like you to do when you find yourself "\
            "somehow ripped from your own "\
            "universe?" % (gender).lower())
print (" ")
print (" ")
slow_print ("crunch...")
print (" ")
print (" ")
slow_print ("crunch...")
print (" ")
print (" ")
slow_print ("crunch...")
print (" ")
print (" ")
slow_print ("*Everything is dark. You hear someone approaching.*")
print (" ")
print (" ")
slow_print ("???: Hey look at this! It's a " + gender.lower() + "!")
print (" ")
print (" ")
slow_print ("*A hand falls on your shoulder and shakes you. "\
            "Your eyes snap open, instantly explaining the reason " \
            "for the earlier darkness, bringing to view a large forest. " \
            "A pair of red-heads in goth attire, looking " \
            "nearly identical to one another, "\
            "are staring down at you curiously.*")
print (" ")
print (" ")
slow_print ("???: Woah! *The one farthest from you exclaims, scratching at"\
            "his head* You're not another Jack.")
print (" ")
print (" ")
slow_print ("*You look at the man confused. What was a Jack?" \
            " Did he mean like in a deck of cards?*")
print (" ")
print (" ")
slow_print ("???: *The closer man, the one who'd shaken you awake, "\
            "gave a grin at his counterpart before looking back to you.*"\
            " Yeah, you're sure not a Jack. *He abruptly stuck his hand "\
            "out to you.* I'm Animack.")
print (" ")
print (" ")
slow_print ("???: Or you can call him Mog! *the still unnamed man said as"\
            " if it was the best joke he'd ever heard.* I'm Bat, by the way.")
print (" ")
print (" ")
slow_print ("Animack: *The now named Animack shot Bat a dirty glare* Ignore him. "\
            "*His attention returned to you an he began to assist you up "\
            "off the forest floor.* So what's your name?")
print (" ")
print (" ")

charaName = str(raw_input("Input name: "))
print (" ")

slow_print ("Bat: " + charaName + " huh...? *His face crinkled in a "\
            "thoughtful expression* I like it!")
print (" ")
print (" ")
slow_print ("Animack: Yeah yeah, well come on. We better take you in. "\
            "Hot Dad's gonna be pissed somebody else got in.")
print (" ")
print (" ")
slow_print ("Bat: Naahhh, I bet he'd like you! *He said cheerfully "\
            "before pausing to snatch a few sprigs of a seemingly random plant*"\
            " Come on!")

print (" ")
print (" ")
imgoing = gowithtoschool()
print (" ")
if imgoing == "y":
    #staying with Bat and Animack
    slow_print ("*You follow Bat and Animack through the woods, occasionally "\
            "pausing as Bat stops to pluck some random plant life to shove "\
            "in his pockets.*")
    print (" ")
    print (" ")
    askhimnow()
    print (" ")
    print_totals()

#go for the bears  
if imgoing != "y":    
    print (" ")
    slow_print ("Animack: *Animack scowls at you and quickly turns on his heel "\
                "free hand going up to grab Bat's shoulder.* fine, suit yourself! "\
                "I hope you get eaten. *he continues to grumble as he leaves you "\
                "standing alone among the trees.* Stupid " + gender.lower() + ".")
    print (" ")
    print (" ")
    slow_print ("*You huff and turn on your heels. What a jerk! You decide "\
                "you can get on FINE without those two. You take two steps "\
                "forward, in the opposite direction Animack and Bat had gone "\
                "when a loud road interrupts your angry thoughts.*")
    print (" ")
    print (" ")
    newchoice = ontheotherhand()
    if newchoice == "y":
        print newchoice
    else:
        print newchoice
    print (" ")
    print_totals()



