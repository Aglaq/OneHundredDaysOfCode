import time
from turtle import Turtle
from random import randint, random
from car import Car

STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10
# Difficulty: bigger number = easier game, less probability to spawn a car (needs to INT bigger than 0)
DIFFICULTY = 6 


class CarManager(Turtle):
    
    def __init__(self):
        self.cars = []
        self.move_distance = STARTING_MOVE_DISTANCE

    def create_car(self):
        y = randint(-250, 250)
        car = Car((300, y))
        self.cars.append(car)

    def maybe_create_car(self):
        if randint(1, DIFFICULTY) == 1:
            self.create_car()

    def move(self):
        for car in self.cars:
            car.forward(self.move_distance)

    def level_up(self):
        self.move_distance += MOVE_INCREMENT