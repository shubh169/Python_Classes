import art
from game_data import data
import random

print(art.logo)


game_start=True
score=0
while game_start:
    player1=random.choice(data)
    print(f"Compare A: {player1['name']},a {player1['description']},from {player1['country']}.")
    print(art.vs)
    player2=random.choice(data)
    print(f"Againest B: {player2['name']},a {player2['description']},from {player2['country']}.")
    player1_follow_count=int((player1['follower_count']))
    player2_follow_count=int((player2['follower_count']))
    choice=input("Who has more follors? Type 'A' or 'B':").lower()
    if choice =='a':
        if player1_follow_count>player2_follow_count:
            score+=1
            print(f"you're right.current score {score}.")
        else:
            print(f"You are wrong, Game over.Your final score is {score}.")
            game_start=False
    elif choice=='b':
        if player2_follow_count>player1_follow_count:
            score+=1
            print(f"you're right.current score {score}.")
        else:
            print(f"You are wrong, Game over.Your final score is {score}.")
            game_start=False
    else:
        print(f"You choose wrong character.Game over.Your final score is {score}.")
        game_start=False
