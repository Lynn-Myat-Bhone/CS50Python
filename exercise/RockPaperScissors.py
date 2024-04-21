import random

choices = ["Rock","Paper","Scissor"]
computer = random.choice(choices)

print(computer)

player = input("Rock, Paper, Scissor: ").title()

if player.__eq__(computer) : # the same as ==
    print("Computer: ",computer)
    print("Player  :",player)
    print("Tie")
elif player=="Rock":
    if computer=="Scissor":
        print("Computer: ",computer)
        print("Player  :",player)
        print("win")
    if computer=="Paper":
        print("Computer: ",computer)
        print("Player  :",player)
        print("Lose")
elif player == "Paper":
    if computer=="Scissor":
        print("Computer: ",computer)
        print("Player  :",player)
        print("Lose")
    if computer=="Rock":
        print("Computer: ",computer)
        print("Player  :",player)
        print("Win")
elif player == "Scissor":
    if computer=="Rock":
        print("Computer: ",computer)
        print("Player  :",player)
        print("Lose")
    if computer=="Paper":
        print("Computer: ",computer)
        print("Player  :",player)
        print("Win")
else:
    print("Something was wrong")