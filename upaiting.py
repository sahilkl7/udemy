# import colorgram
import random
from turtle import Turtle,Screen
timmy = Turtle()
timmy.speed(0)
my_screen = Screen()
my_screen.colormode(255)
timmy.ht()
# rgb_color= []
# colors  = colorgram.extract('image.jpg',30)
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r,g,b)
#     rgb_color.append(new_color)
# print(rgb_color)

color_list = [ (197, 7, 71), (195, 164, 13), (201, 75, 15), (231, 54, 132), (110, 179, 216), (217, 163, 101), (27, 105, 168), (35, 186, 109), (19, 29, 168), (13, 23, 66), (212, 135, 177), (233, 223, 7), (199, 33, 132), (13, 183, 212), (230, 166, 199), (126, 189, 162), (8, 49, 28), (40, 132, 77), (128, 219, 232), (58, 12, 25), (67, 22, 7), (114, 90, 210), (146, 216, 199), (179, 17, 8), (233, 66, 34)]
step_size = 30
row_size = 10
column_size = 10


for row in range(row_size):
    for column in range(column_size):
        timmy.penup()
        timmy.goto(column*step_size,row*step_size)
        timmy.pendown()
        timmy.dot(20,random.choice(color_list))

my_screen.exitonclick()