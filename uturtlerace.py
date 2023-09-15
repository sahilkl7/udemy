from turtle import Turtle, Screen
import random

is_race_on = False
my_screen = Screen()
my_screen.setup(width=500, height=400)

user_bet = my_screen.textinput(title='Make your bet', prompt='Which turtle will win the race? Enter the color: ')
print(user_bet)

colors = ['green', 'red', 'blue', 'purple', 'yellow', 'orange']
all_turtles = []

for i in range(6):
    new_turtle = Turtle(shape='turtle')
    new_turtle.color(colors[i])
    new_turtle.penup()
    new_turtle.goto(x=-230, y=-100 + i * 30)
    all_turtles.append(new_turtle)

if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor()> 230:
            is_race_on =False
            winning_turtle = turtle.pencolor()
            if winning_turtle ==user_bet:
                print(f"You've won.The {winning_turtle} turtle is the winner!")
            else:
                print(f"You've have lost!.The {winning_turtle} turtle is the winner!")

        rand_distance = random.randint(0, 10)
        turtle.forward(rand_distance)

my_screen.exitonclick()
