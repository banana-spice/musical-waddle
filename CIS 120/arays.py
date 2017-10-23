from random import *
aryLottery = []
nerms = int(raw_input("How many numbers? "))
for i in range(nerms):
    numb = randint(1,100)
    aryLottery.append(numb)

length = len(aryLottery)    


for j in range(length):
    print aryLottery[j]
