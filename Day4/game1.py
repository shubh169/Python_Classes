import random

choice=int(input("What do you choose? Type 0 for Rock, 1 for Paper and 2 for Scissors."))
lst=["Rock","Paper","Scissors"]
user_choice=lst[choice]
print(F"User choose:{user_choice}.")
system_choice=random.choice(lst)
print(f"System choose:{system_choice}.")
if (user_choice=="Rock" and system_choice=="Scissors") or (user_choice=="Scissors" and system_choice=="Paper") or (user_choice=="Paper" and system_choice=="Rock"):
    print("You Win.")
elif (user_choice=="Rock" and system_choice=="Rock") or (user_choice=="Scissors" and system_choice=="Scissors") or (user_choice=="Paper" and system_choice=="Paper"):
    print("Match Draw")
else:
    print("You Loss.")



