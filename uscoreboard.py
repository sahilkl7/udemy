from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        with open('data.txt') as f:
            self.high_score = int(f.read())
        self.color('white')
        self.hideturtle()
        self.penup()
        self.goto(0, 270)
        self.update_score()

    def update_score(self):
        self.clear()
        self.write(f"Score : {self.score} HighScore : {self.high_score} ", move=False, align='center', font=('Courier', 20, 'normal'))

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open('data.txt' , 'w') as f:
                f.write(f"{self.high_score}")

        self.score = 0
        self.update_score()

    # def game(self):
    # self.color('white')
    # self.goto(0,0)
    # self.write("Game Over.",move = False,align='center',font=('Courier',20,'normal'))

    def track_score(self):
        self.score += 1
        self.update_score()
