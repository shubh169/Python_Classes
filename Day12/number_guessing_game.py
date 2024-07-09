import random
from art import logo
print(logo)

print("Welcome to the Number Guessing Game!")
print("I am thinkin of a number between 1 and 100.")

random_number=random.randint(1,100)
level=input("Choose a difficulty. type 'easy' or 'hard' to guess the game:").lower()
live=0
if level=='easy':
    live=10
    print(f"You have {live} attempts remaining to guess the number.")
elif level=='hard':
    live=5
    print(f"You have {live} attempts remaining to guess the number.")
else:
    print("You choose a wrong level of game.")
   
while live:
    guess=int(input("Please make a guess:"))
    if guess>random_number:
        print("Too High")
        live-=1
        print(f"You have {live} attempts remaining to guess the number.")
    elif guess<random_number:
        print("Too small")
        live-=1
        print(f"You have {live} attempts remaining to guess the number.")
    else:
        print("You win")
        break
if live==0:
    print("You've run out of guess, you loss.")