from turtle import Turtle,Screen

timmy=Turtle()
screen=Screen()

def move_forward():
    timmy.forward(10)

screen.listen()
screen.onkeypress(key="space",fun=move_forward)
screen.exitonclick()
