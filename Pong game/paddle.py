from turtle import Turtle

class Paddle:

    def __init__(self, positions):
        self.segments = []
        self.create_paddle(positions)

    def create_paddle(self, positions):
        for pos in positions:
            segment = Turtle("square")
            segment.color("white")
            segment.penup()
            segment.goto(pos)
            self.segments.append(segment)

    def move_up(self):
        for segment in self.segments:
            segment.setheading(90)
            segment.forward(20)

    def move_down(self):
        for segment in self.segments:
            segment.setheading(270)
            segment.forward(20)
