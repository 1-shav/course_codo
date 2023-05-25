import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
car_mananger = CarManager()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(player.move, "Up")


game_is_on = True
while game_is_on:
    time.sleep(0.05)
    screen.update()
    car_mananger.generate_car()
    car_mananger.move_cars()

    #detect collision with car
    for car in car_mananger.all_cars:
        if player.distance(car) < 23:
            player.dead()
            scoreboard.game_over()
            screen.update()
            game_is_on = False

    #detect successful crossing
    if player.is_at_finish_line():
        player.go_to_start()
        car_mananger.level_up()
        scoreboard.increase_level()

        
screen.exitonclick()