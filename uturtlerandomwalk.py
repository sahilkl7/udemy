import random
import turtle
from turtle import  Screen,Turtle

timmy = Turtle()
turtle.colormode(255)

def random_color():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    color = (r,g,b)
    return color
print(timmy)
timmy.width(10)
timmy.speed(0)

directions = [0,90,180,270]

for _ in range(200):
    timmy.forward(30)
    timmy.setheading(random.choice(directions))
    timmy.color(random_color())

my_screen = Screen()
my_screen.exitonclick()