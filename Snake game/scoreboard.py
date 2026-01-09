from turtle import Turtle

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.highscore = 0
        self.penup()
        self.hideturtle()
        self.goto(0, 260)
        self.update_score()

    def update_score(self):
        self.clear()
        self.write(f"Score: {self.score}" + f" HighScore: {self.highscore}", align="center",
                   font=("Arial", 18, "normal"))

    def increase_score(self):
        self.score += 1
        self.update_score()


    def reset(self):
        if self.score > self.highscore:
            self.highscore = self.score
        self.score = 0
        self.update_score()

    # def gameover(self):
    #     self.goto(0, 0)
    #     self.write("GAME OVER", align="center",
    #                font=("Arial", 24, "normal"))
