import random
import turtle
from turtle import Turtle ,Screen

timmy = Turtle()
print(timmy)
timmy.speed(0)
turtle.colormode(255)


def random_color():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    color = (r,g,b)
    return color

for _ in range(100):
    timmy.circle(100)
    timmy.left(5)
    timmy.color(random_color())




my_screen = Screen()
my_screen.exitonclick()
