from turtle import Turtle,Screen
import random


timmy = Turtle()
print(timmy)

colour_list = ['red','blue','green','yellow','black','cyan','skyblue','lightgreen']

for i in range(3,11):
    number_of_sides = i
    angle = 360 / number_of_sides
    timmy.color(random.choice(colour_list))
    for _ in range(i):
        timmy.right(angle)
        timmy.forward(100)

screen = Screen()
screen.exitonclick()