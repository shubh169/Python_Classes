from turtle import Turtle
starting_position=(0,-280)
move_distance=10
Finish_line_Y=280
class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.color("green")
        self.go_to_start()
        self.setheading(90)


    def move_up(self):
        self.forward(move_distance)

    def go_to_start(self):
        self.goto(starting_position)

    def is_it_fininsh_line(self):
        if self.ycor() > Finish_line_Y:
            return True
        else:
            return False
