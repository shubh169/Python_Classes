from turtle import Turtle
import random
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
Starting_move_distance=5
class CarManager(Turtle):
    def __init__(self):
        self.all_cars=[]
        self.car_speed=Starting_move_distance

    def create_cars(self):
        random_chance=random.randint(1,6)
        if random_chance==1:
            new_car=Turtle("square")
            new_car.shapesize(stretch_wid=1,stretch_len=2)
            new_car.penup()
            new_car.color(random.choice(colors))
            random_y=random.randint(-250,250)
            new_car.goto(400,random_y)
            self.all_cars.append(new_car)



    def move_cars(self):
        for car in self.all_cars:
            car.backward(self.car_speed)


    def increase_speed(self):
        self.car_speed+=Starting_move_distance




