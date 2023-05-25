from cgitb import reset
from turtle import Screen
from snek_logic import Snek
from food_logic import Food
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("snek_game...")
screen.tracer(0)

saap = Snek()
khana = Food()
score = Scoreboard()

screen.listen()
screen.onkey(saap.up, "Up")
screen.onkey(saap.down, "Down")
screen.onkey(saap.left, "Left")
screen.onkey(saap.right, "Right")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)

    saap.move()

    #detect collision with food
    if saap.head.distance(khana) < 18:
        khana.refresh()
        saap.extend()
        score.increase_score()
        

    #detect collision with wall
    if saap.head.xcor() > 299 or saap.head.xcor() < -299 or saap.head.ycor() > 299 or  saap.head.ycor() < -299:
        score.reset()
        saap.reset()

    #detect collision with tail
    for segment in saap.segments[1:]:
        if saap.head.distance(segment) < 10:
            score.reset()
            saap.reset()

screen.exitonclick()