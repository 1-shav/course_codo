from turtle import Turtle
from random import choice, randint

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 5


class CarManager:
    
    def __init__(self):
        self.all_cars = []
        self.car_speed = STARTING_MOVE_DISTANCE


    def generate_car(self):
        chance = randint(1, 6)
        if chance == 1:
            new_car = Turtle("square")
            new_car.shapesize(stretch_wid=1, stretch_len=2)
            new_car.penup()
            new_car.color(choice(COLORS))
            random_y = randint(-250, 250)
            new_car.goto(300, random_y)
            if self.all_cars != []:
                for previous_car in self.all_cars[-10:]:
                    while new_car.distance(previous_car) < 35:
                        random_y = randint(-250, 250)
                        new_car.goto(300, random_y)
            new_car.setheading(180)
            self.all_cars.append(new_car)

    def move_cars(self):
        for car in self.all_cars:
            random_speed = randint(5, self.car_speed)
            car.forward(random_speed)

    def level_up(self):
        self.car_speed += MOVE_INCREMENT