from turtle import Turtle
import random

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.goto(0, 0)
        self.direction = random.randint(0, 359)

    def move(self):
        self.setheading(self.direction)
        self.forward(15)

    def bounce_y(self):
        # reverse the vertical direction
        self.direction = 360 - self.direction

    def bounce_x(self):
        # reverse the horizontal direction
        self.direction = 180 - self.direction
