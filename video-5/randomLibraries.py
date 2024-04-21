import random #from random import choice
# There are lots of third part modules called packages //web named (pyip)
list =["Head","Tail"]
coin = random.choice(list)
print(coin)

number = random.randint(1,5) # random from 1 to 5
print(number)

cards = ["Jack","King","Queen"]
random.shuffle(cards)
for i in cards:
    print(i)