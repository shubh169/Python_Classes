from turtle import Turtle,Screen
import random

colours = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat",
           "SlateGray", "SeaGreen"]
timmy=Turtle()
timmy.shape("turtle")
timmy.color("red")
def drew_shape(shape):
    angle=360/shape
    for i in range(shape):
        timmy.forward(100)
        timmy.right(angle)



for shape in range(3,12):
    timmy.color(random.choice(colours))
    drew_shape(shape)

screen=Screen()
screen.exitonclick()