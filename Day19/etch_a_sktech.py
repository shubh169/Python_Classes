from turtle import Turtle,Screen

timmy=Turtle()
screen=Screen()

def move_forward():
    timmy.forward(10)
def move_backward():
    timmy.backward(10)

def move_left():
    new_heading = timmy.heading()+10
    timmy.setheading(new_heading)

def move_right():
    new_heading = timmy.heading()-10
    timmy.setheading(new_heading)

def clear_screen():
    timmy.clear() 
    timmy.penup()
    timmy.home()
    timmy.pendown()

screen.listen()
screen.onkeypress(key="w",fun=move_forward)
screen.onkeypress(key="s",fun=move_backward)
screen.onkeypress(key="a",fun=move_right)
screen.onkeypress(key="d",fun=move_left)
screen.onkeypress(key="c",fun=clear_screen)
screen.exitonclick()
