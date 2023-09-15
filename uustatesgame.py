import pandas
import turtle

screen = turtle.Screen()
screen.title('U.S StateGame')
image = 'blank_states_img.gif'
screen.addshape(image)
turtle.shape(image)

#
# def mouse_on_click(x,y):
#     print(x,y)
#
# turtle.onscreenclick(mouse_on_click)
#
# turtle.mainloop()
is_game_on = True
data = pandas.read_csv('50_states.csv')
guessed_states = []


all_states = data['state'].to_list()

while len(guessed_states) < 50:
    answer_input = screen.textinput(title=f"({len(guessed_states)}/50 Guess the state's",prompt="Guess the another state")

    if answer_input in all_states:
        guessed_states.append(answer_input)
    if answer_input == 'Exit':

        missing_states = [state for state in all_states if state not in guessed_states]
        # missing_states = []

        # for state in all_states:
        #     if state not in guessed_states:
        #         missing_states.append(state)
        data_states = pandas.DataFrame(missing_states)
        data_states.to_csv('States_To_Learn.csv') #will create a new csv file with one column

        break

        answer_input.title()
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == answer_input]
        t.goto(int(state_data.x),int(state_data.y))
        answer_input.istitle()
        t.write(answer_input)



