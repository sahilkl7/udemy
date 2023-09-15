from turtle import Turtle, Screen
from upaddle import Paddle
from uball import Ball
import time
from upongscore import Score

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor('black')
screen.title('Pong Game')
screen.tracer(0)
r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))

ball = Ball()
score = Score()
screen.listen()

screen.onkey(r_paddle.go_up, 'Up')
screen.onkey(r_paddle.go_down, 'Down')
screen.onkey(l_paddle.go_up, 'w')
screen.onkey(l_paddle.go_down, 's')

game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    # Detect Collision With The Wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bouncey()

    # Detect Collision with the paddle
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320:
        ball.bouncex()


    if ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.bouncex()

    # Detect when r_paddle misses the ball
    if ball.xcor() > 380:
        ball.reset_position()
        score.l_point()

    # Detect when l_paddle misses the ball
    if ball.xcor() < -380:
        ball.reset_position()
        score.r_point()


screen.exitonclick()
