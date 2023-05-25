from random import randint
from turtle import Turtle, Screen

display = Screen()
display.setup(width=500, height=400)
user_bet = display.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a colour")
colors = ["red","orange", "yellow", "green", "blue", "purple"]
our_turtles = []
race_is_on = False
y = -100

for colour in colors:
    new_turtle = Turtle(shape="turtle")
    new_turtle.penup()
    new_turtle.color(colour)
    new_turtle.goto(x=-230, y=y)
    our_turtles.append(new_turtle)
    y += 40

if user_bet:
    race_is_on = True

while race_is_on:
    for turtle in our_turtles:
        if turtle.xcor() > 230:
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You have WON. The winning turtle was {winning_color}!")
            else:
                print(f"You have LOST. The winning turtle was {winning_color}!")
            race_is_on = False
        random_distance = randint(0, 10)
        turtle.forward(random_distance)

display.exitonclick()