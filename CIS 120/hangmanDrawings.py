import random

HANGMAN = [
    """
        ---
       |   |
       |
       |
       |
       |
       |
       |
    --------
    """,
    """
        ---
       |   |
       |   0
       |
       |
       |
       |
       |
       |
    --------
    """,
    """
        ---
       |   |
       |   0
       |  -+-
       |
       |
       |
       |
       |
    --------
    """,
    """
        ---
       |   |
       |   0
       | /-+-
       |
       |
       |
       |
       |
    --------
    """,
    """
        ---
       |   |
       |   0
       | /-+-\\
       |
       |
       |
       |
       |
    --------
    """,
    """
        ---
       |   |
       |   0
       | /-+-\\
       |   |
       |
       |
       |
       |
    --------
    """,
    """
        ---
       |   |
       |   0
       | /-+-\\
       |   |
       |   |
       |
       |
       |
    --------
    """,
    """
        ---
       |   |
       |   0
       | /-+-\\
       |   |
       |   |
       |  |
       |  |
       |
    --------
    """,
    """
        ---
       |   |
       |   0
       | /-+-\\
       |   |
       |   |
       |  | |
       |  | | 
       |
    --------
    """]
WORDS = ["ROBOJACK","ANIMACK","VOID","MOON",
         "MARSHMALLOW","SPECTER","HIPPIE",
         "GHOUL","SNAKE","BATFAMILIAR","CATDEMON",
         "CORRUPTGJ","GACK","DRAGONKID","JIANYU",
         "HOTDAD","DJACKO","GOOEY","COTARD","SIREN",
         "SKELETON","CORPSE","BEAN","VAMPIRE",
         "WEREWOLF","ACCIDENTAL"]

word = random.choice(WORDS)
so_far = "-" * len(word)
print so_far
wrong = 0
used = []
MAX_WRONG = len(HANGMAN) - 1

print "Welcome to Hang-Jack!!! Have fun~"

while wrong < MAX_WRONG and so_far != word:
    print HANGMAN[wrong]
    print "You've guessed the letters: ", used
    print so_far
    #get guess
    guess = raw_input("Enter your guess *Lady Macbeth voice*: ")
    guess = guess.upper()

    #check guess
    while guess in used:
        print "You've already guessed ", guess
        guess = raw_input("Guess again *Lady Macbeth intensifies*: ")
        guess = guess.upper()
    used.append(guess)

    #compare guess to generated word
    if guess in word:
        print "Booyah!"
        new = " "
        for i in range(len(word)):
            if guess == word[i]:
                new += guess
            else:
                new += so_far[i]
        so_far = new
    else:
        print "Too bad so sad!"
        wrong += 1
        
if wrong == MAX_WRONG:
    print HANGMAN[wrong]
    print "You've been jacked!"
else:
    print "Sweet victory!"
print "The word was", word

raw_input("Enter any Key to finish.")
