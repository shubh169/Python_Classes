from turtle import Turtle,Screen

timmy=Turtle()
timmy.shape("turtle")
timmy.color("black")

for _ in range(15):
    timmy.forward(10)
    timmy.color("white")
    timmy.forward(10)
    timmy.color("black")





screen=Screen()
screen.exitonclick()