from turtle import Turtle,Screen
import random


screen = Screen()
is_race_on = False

screen.setup(width=500,height=400)
user_bet = screen.textinput(title="Make A Bet",prompt="Which turtle will win the race? Enter a color: ")

color = ["red","green","blue","orange","purple","yellow"]

postion_Y = -125
all_turtle = []



for turtle in range(0,6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(color[turtle])
    new_turtle.penup()
    new_turtle.goto(x=-200,y=postion_Y)
    postion_Y +=50
    all_turtle.append(new_turtle)
    



if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in all_turtle:
        if turtle.xcor() > 230 :
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You Have Won .The {winning_color} turtle is winner")
                is_race_on = False 
            else:
                print(f"You Have Loss .The {winning_color} turtle is winner") 
            is_race_on = False       
        random_distance = random.randint(1,10)
        turtle.forward(random_distance)
     

screen.exitonclick()