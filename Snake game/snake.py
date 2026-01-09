from turtle import Turtle

STARTING_POSITION = [(0,0), (-20,0), (-40,0)]
MOVE_DISTANCE = 20

UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake:

    def __init__(self):
        self.snakes = []
        self.create_snake()
        self.head = self.snakes[0]

    def create_snake(self):
        for position in STARTING_POSITION:
            self.add_segment(position)

    def add_segment(self, position):
        snake_piece = Turtle("square")
        snake_piece.penup()
        snake_piece.color("green")
        snake_piece.goto(position)
        self.snakes.append(snake_piece)

    def extend(self):
        self.add_segment(self.snakes[-1].position())

    def move(self):
        for piece in range(len(self.snakes)-1, 0, -1):
            new_x = self.snakes[piece-1].xcor()
            new_y = self.snakes[piece-1].ycor()
            self.snakes[piece].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)

    def reset(self):
        for seg in self.snakes:
            seg.goto(1000,1000)
        self.snakes.clear()
        self.create_snake()
        self.head = self.snakes[0]

    def move_up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def move_down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def move_left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def move_right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
