from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
from line import CenterLine
import time

# Screen setup
screen = Screen()
screen.setup(width=600, height=600)
screen.title("Pong Game")
screen.bgcolor("black")
screen.tracer(0)

# Objects
right_paddle = Paddle((280, 0))
left_paddle = Paddle((-280, 0))
ball = Ball()
scoreboard = Scoreboard()
center_line = CenterLine()

# Controls
screen.listen()
screen.onkeypress(right_paddle.up, "Up")
screen.onkeypress(right_paddle.down, "Down")
screen.onkeypress(left_paddle.up, "w")
screen.onkeypress(left_paddle.down, "s")

game_is_on = True
while game_is_on:
    time.sleep(0.03)
    screen.update()
    ball.move()

    # Wall collision
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # Right paddle collision
    if ball.distance(right_paddle) < 50 and ball.xcor() > 260:
        ball.bounce_x()

    # Left paddle collision
    if ball.distance(left_paddle) < 50 and ball.xcor() < -260:
        ball.bounce_x()

    # Right miss → Left scores
    if ball.xcor() > 300:
        ball.reset_position()
        scoreboard.left_point()

    # Left miss → Right scores
    if ball.xcor() < -300:
        ball.reset_position()
        scoreboard.right_point()

    # GAME OVER check AFTER scoring
    if scoreboard.left_score == 10 or scoreboard.right_score == 10:
        screen.update()          # force drawing before exiting
        scoreboard.game_over()
        game_is_on = False
                                