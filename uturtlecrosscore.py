from turtle import Turtle

class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.penup()
        self.hideturtle()
        self.goto(-280,250)
        self.write_score()

    def write_score(self):
        self.clear()
        self.write(f'Level :{self.score}',align='Left',font = ("Courier",24,'normal'))

    def update_score(self):
        self.score += 1
        self.write_score()

    def game_over(self):
        self.goto(0,0)
        self.write(f'GAME OVER',align='center',font = ("Courier",24,'normal'))
