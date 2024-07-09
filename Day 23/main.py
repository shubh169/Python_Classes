from turtle import Screen
from player import Player
from scoreboard import Scoreboard
from car_manager import CarManager
import time

# Screen Setup.
screen = Screen()
screen.setup(width=800,height=600)
screen.bgcolor("white")
screen.title("Turtle Crossing Game")
screen.tracer(0)

player=Player()
scoreboard=Scoreboard()
cars_manager=CarManager()
screen.listen()
screen.onkey(player.move_up,"Up")


is_game_on=True
while is_game_on:
    time.sleep(0.1)
    screen.update()
    cars_manager.create_cars()
    cars_manager.move_cars()

    # Detect Collision with Cars.
    for cars in cars_manager.all_cars:
        if cars.distance(player)<20:
            is_game_on=False
            scoreboard.game_over()

    # Detect successfully crossing the cars.
    if player.is_it_fininsh_line():
        player.go_to_start()
        scoreboard.update_score()
        cars_manager.increase_speed()


screen.exitonclick()