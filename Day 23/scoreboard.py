from turtle import Turtle
ALIGNMENT ='center'
FONT =('bold', 15, 'normal')
class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("black")
        self.penup()
        self.hideturtle()
        self.score =0
        self.goto(-360,270)
        self.update_score()

    def update_score(self):
        self.clear()
        self.score+=1
        self.write(f"Level:{self.score}", align=ALIGNMENT, font=FONT)


    def game_over(self):
        self.goto(0, 0)
        self.write(f"Game Over", align=ALIGNMENT, font=FONT)
