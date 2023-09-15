from turtle import Turtle,Screen

tim = Turtle()
tim.shape('turtle')
tim.color('green')
tim.width(10)

def move_forward():
    tim.forward(100)
def move_backward():
    tim.backward(100)
def move_left():
    new_heading = tim.heading() + 10 # same as tim.left(10)
    tim.setheading(new_heading)
def move_right():
    new_heading = tim.heading() - 10 # same as tim.right(10)
    tim.setheading(new_heading)
def clear():
    tim.clear()
    tim.penup()
    tim.home()
    tim.pendown()

my_screen = Screen()
my_screen.listen()
my_screen.onkey(move_forward,'w')
my_screen.onkey(move_backward,'s')
my_screen.onkey(move_left,'a')
my_screen.onkey(move_right,'d')
my_screen.onkey(clear,'c')
my_screen.exitonclick()
