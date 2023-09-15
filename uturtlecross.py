from turtle import Turtle, Screen
from uturtleplayer import Player
from uturtlecar import CarManager
from uturtlecrosscore import Score

import time

screen = Screen()
player = Player()
car_manager = CarManager()
score= Score()

screen.tracer(0)
screen.setup(width=600, height=600)
screen.title('Turtle Crossing')
screen.listen()
screen.onkey(player.go_up, 'Up')

is_game_on = True
while is_game_on:
    time.sleep(0.1)
    screen.update()
    car_manager.create_cars()
    car_manager.move_car()

    # Detect a collision with the car
    for car in car_manager.all_cars:
        if car.distance(player) < 20:
            is_game_on = False
            score.game_over()

    # Detect a successful crossing
    if player.is_at_finish_line():
        player.go_to_start()
        car_manager.level_up()
        score.update_score()


screen.exitonclick()
