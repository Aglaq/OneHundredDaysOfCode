# Day 21 - Build the Snake Game Part 2: Inheritance & List Slicing
# Day 21 - Project: Snake Game

# Examples and exercises from day 21
class Animal:
    def __init__(self):
        self.num_eyes = 2

    def breathe(self):
        print("Inhale, exhale.")

class Fish(Animal):
    def __init__(self):
        super().__init__()

    def swim(self):
        print("Moving in water.")

nemo = Fish()
nemo.swim()
nemo.breathe()