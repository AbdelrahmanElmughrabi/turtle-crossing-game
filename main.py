import time
from turtle import Screen

import car_manager
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

game_is_on = True
player=Player()
scoreboard=Scoreboard()

screen.listen()
screen.onkey(fun=player.up,  key="Up")

while game_is_on:
    time.sleep(0.1)
    screen.update()
    car = CarManager()
    car.move()

    if player.ycor()>=280:
        scoreboard.increment_score()
        car.leve_up()
        player.reset_pos()



    for car in car_manager.car_list:
        if car.distance(player) < 20:
            scoreboard.gameOver()
            game_is_on=False


screen.exitonclick()