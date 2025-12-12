from turtle import Turtle

class CenterLine(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(0, 300)
        self.setheading(270)
        self.draw_line()

    def draw_line(self):
        for _ in range(25):
            self.pendown()
            self.forward(20)
            self.penup()
            self.forward(20)
