from turtle import Screen
from paddle import Paddle
from ball import Ball
import random
import time

POSITION_RIGHT = [(280, 40), (280, 20), (280, 0)]
POSITION_LEFT  = [(-280, 40), (-280, 20), (-280, 0)]
DIRCTION = random.randint(0,359)

screen = Screen()
screen.title("PONG GAME")
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)

right_paddle = Paddle(POSITION_RIGHT)
left_paddle = Paddle(POSITION_LEFT)

ball = Ball()

# Controls
screen.listen()
screen.onkeypress(right_paddle.move_up, "Up")
screen.onkeypress(right_paddle.move_down, "Down")

screen.onkeypress(left_paddle.move_up, "w")
screen.onkeypress(left_paddle.move_down, "s")


game_is_on = True
while game_is_on:
    time.sleep(0.05)
    screen.update()
    ball.move()

    # collision with wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()


        
