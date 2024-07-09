from turtle import Turtle,Screen
import random

screen=Screen()
screen.setup(700,500)
is_race_on=False
user_guess=screen.textinput(title="Make your Bet",prompt="which turtle win the race? Enter a color:")
colors=["red","orange","yellow","green","blue","purple"]
y_positions=[-70,-40,-10,20,50,80]
all_turtle=[]

for i in range(6):
    New_turtle=Turtle(shape="turtle")
    New_turtle.penup()
    New_turtle.color(colors[i])
    New_turtle.goto(x=-330, y=y_positions[i])
    all_turtle.append(New_turtle)

if user_guess:
    is_race_on=True

while is_race_on:
    for turtle in all_turtle:
        if turtle.xcor()>330:
            is_race_on=False
            winning_color=turtle.pencolor()
            if user_guess==winning_color:
                print(f"You've won! The {winning_color} turtle won the game!")
            else:
                print(f"You've lost! The {winning_color} turtle won the game!")

        rand_distance=random.randint(0,10)
        turtle.forward(rand_distance)

screen.exitonclick()