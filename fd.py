import turtle

# Create a turtle named "timmy"
timmy = turtle.Turtle()

# Set the step size and number of rows and columns
step_size = 20
num_rows = 10
num_columns = 10

# Loop to draw the grid of dots
for row in range(num_rows):
    for column in range(num_columns):
        timmy.penup()  # Lift the pen
        timmy.goto(column * step_size, row * step_size)  # Move to the current position
        timmy.dot(10)  # Draw a dot

# Create a screen
my_screen = turtle.Screen()

# Exit the program when clicking on the screen
my_screen.exitonclick()
