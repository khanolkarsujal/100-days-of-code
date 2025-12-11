from turtle import Turtle

STARTING_POSITION = [(0,0), (-20,0), (-40,0)]

UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake:

    def __init__(self):
        self.snakes = []
        self.create_snake()

    def create_snake(self):
        for position in STARTING_POSITION:
            snake_piece = Turtle("square")
            snake_piece.penup()
            snake_piece.color("green")
            snake_piece.goto(position)
            self.snakes.append(snake_piece)

    def move(self):
        for piece in range(len(self.snakes)-1, 0, -1):
            new_x = self.snakes[piece-1].xcor()
            new_y = self.snakes[piece-1].ycor()
            self.snakes[piece].goto(new_x, new_y)
        self.snakes[0].forward(20)

    def move_up(self):
        if self.snakes[0].heading() != DOWN:
            self.snakes[0].setheading(UP)

    def move_down(self):
        if self.snakes[0].heading() != UP:
            self.snakes[0].setheading(DOWN)

    def move_left(self):
        if self.snakes[0].heading() != RIGHT:
            self.snakes[0].setheading(LEFT)

    def move_right(self):
        if self.snakes[0].heading() != LEFT:
            self.snakes[0].setheading(RIGHT)
