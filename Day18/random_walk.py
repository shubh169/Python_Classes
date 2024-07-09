
from turtle import Turtle,Screen
import random

colours = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat",
           "SlateGray", "SeaGreen"]

timmy =Turtle()
timmy.shape("turtle")
timmy.pensize(15)
timmy.speed("fastest")

directions = [0,90,180,270]
for _ in range(100):
    timmy.color(random.choice(colours))
    timmy.forward(30)
    timmy.setheading(random.choice(directions))





screen=Screen()
screen.exitonclick()