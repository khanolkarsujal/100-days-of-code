from turtle import Turtle, Screen
import random
import turtle
import colorgram
import os


turtle.colormode(255)

# Get current path
path = os.getcwd()
print(path)

# Extract colors
"""Note: path will be different.."""
colors = colorgram.extract(f'{path}/dot.jpeg', 30)

# Convert to rgb
rgb_color = []
for color in colors:
    r = color.rgb.r
    g = color.rgb.g
    b = color.rgb.b
    rgb_color.append((r, g, b))   

tim = Turtle()
tim.speed("fastest")
tim.penup()
tim.setpos(-200, -200)

for row in range(10):
    for col in range(10):
        tim.dot(20, random.choice(rgb_color))
        tim.forward(50)
    # Move to next row
    tim.backward(50 * 10)
    tim.left(90)
    tim.forward(50)
    tim.right(90)

screen = Screen()
screen.exitonclick()
