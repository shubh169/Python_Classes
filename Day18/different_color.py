import turtle as t
import random



timmy =t.Turtle()
t.colormode(255)
timmy.shape("turtle")
timmy.pensize(15)
timmy.speed("fastest")

def random_color():
    r = random.randint(0,255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    rndom_color = (r,g,b)
    return rndom_color

directions = [0,90,180,270]
for _ in range(100):
    timmy.color(random_color())
    timmy.forward(30)
    timmy.setheading(random.choice(directions))





screen=t.Screen()
screen.exitonclick()