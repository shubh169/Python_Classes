import random
cards=[11,2,3,4,5,6,7,8,9,10,10,10,10]
user=[]
computer=[]
for i in range(2):
    user.append(random.choice(cards))
    computer.append(random.choice(cards))
