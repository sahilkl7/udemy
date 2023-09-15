from turtle import Turtle,Screen
import random
from ufood import Food
from usnake1 import Snake
from uscoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=600,height=600)
screen.title("My Snake Game")
screen.bgcolor('black')
screen.tracer(0)

snake = Snake()
food = Food()
score = Scoreboard()
screen.listen()

screen.onkey(snake.up,'Up')
screen.onkey(snake.down,'Down')
screen.onkey(snake.left,'Left')
screen.onkey(snake.right,'Right')


game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    # To detect a collision

    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        score.track_score()

    # Detect collision with wall
    if snake.head.xcor() > 285 or snake.head.xcor() < -285 or snake.head.ycor() > 285 or snake.head.ycor() < -285:
        score.reset()
        snake.reset_snake()
    # Detect collision with tail
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            score.reset()
            snake.reset_snake()


screen.exitonclick()