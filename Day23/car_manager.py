import time
from turtle import Turtle
from random import randint, random
from car import Car

STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager(Turtle):
    def __init__(self):
        self.cars = []
        self.move_distance = STARTING_MOVE_DISTANCE

    def create_car(self):
        y = randint(-250, 250)
        car = Car((300, y))
        self.cars.append(car)

    def maybe_create_car(self):
        if randint(1, 6) == 1:
            self.create_car()

    def move(self):
        for car in self.cars:
            car.forward(self.move_distance)

    def level_up(self):
        self.move_distance += MOVE_INCREMENT