from turtle import Turtle

class Paddle(Turtle):

    def __init__(self, position):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=5, stretch_len=1)   # One tall paddle instead of 3 blocks
        self.penup()
        self.goto(position)

    def up(self):
        new_y = self.ycor() + 30
        if new_y < 260:
            self.goto(self.xcor(), new_y)

    def down(self):
        new_y = self.ycor() - 30
        if new_y > -260:
            self.goto(self.xcor(), new_y)
