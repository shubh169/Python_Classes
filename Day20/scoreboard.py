from turtle import Turtle
ALIGNMENT ='center'
FONT =('Arial', 16, 'normal')
class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score=0
        with open("data_text.txt") as data:
            self.highscore=int(data.read())
        self.color("white")
        self.penup()
        self.goto(0, 270)
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score={self.score}  High score {self.highscore}", align=ALIGNMENT, font=FONT)

    def reset(self):
        if self.score > self.highscore:
            self.highscore=self.score
            with open("data_text.txt",mode='w') as data:
                data.write(f"{self.highscore}")
        self.score=0
        self.update_scoreboard()

    # def game_over(self):
    #     self.goto(0,0)
    #     self.write(f"Game Over.", align=ALIGNMENT, font=FONT)
    def increase_score(self):
        self.score+=1
        self.update_scoreboard()