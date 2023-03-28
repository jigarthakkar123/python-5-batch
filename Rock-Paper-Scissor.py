import random

l=["Rock","Paper","Scissor"]
computer=random.choice(l)

user=input("Choice(Rock,Paper, Scissor): ")

if user==computer:
    print("Draw")
elif user=="Rock" and computer=="Paper":
    print("Computer Wins")
elif user=="Paper" and computer=="Scissor":
    print("Computer Wins")
elif user=="Scissor" and computer=="Rock":
    print("Computer Wins")
elif user=="Paper" and computer=="Rock":
    print("User Wins")
elif user=="Scissor" and computer=="Paper":
    print("User Wins")
elif user=="Rock" and computer=="Scissor":
    print("User Wins")
