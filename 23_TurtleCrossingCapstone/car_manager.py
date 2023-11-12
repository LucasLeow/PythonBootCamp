import random
import time
from turtle import Turtle

# blue = slowest, indigo = fastest
COLORS = ['blue', 'green', 'yellow', 'orange', 'red', 'indigo']
DIFFICULTY = {
    'blue': 3,
    'green': 4,
    'yellow': 5,
    'orange': 6,
    'red': 7,
    "indigo": 8
}
START_MOVE_DIST = 5
MOVE_INCREMENT = 30
TOLERANCE = 50


class CarManager:
    def __init__(self, scn_width, scn_height, level):
        self.level = level
        self.scn_width = scn_width
        self.scn_height = scn_height
        self.cars = []

    def generate_car(self):
        SEED_MAX = 8
        if self.level >= 5:
            SEED_MAX = 6
        if self.level >= 10:
            SEED_MAX = 5
        if self.level >= 15:
            SEED_MAX = 4
        if self.level >= 20:
            SEED_MAX = 3

        seed = random.randint(1, SEED_MAX)
        if seed == 1:
            car = Turtle(shape='square')
            car.shapesize(stretch_len=2, stretch_wid=1)
            car.color(random.choice(list(DIFFICULTY.keys())))
            car.penup()
            car.speed('fastest')

            y_cor = random.randint(-self.scn_height // 2 + TOLERANCE, self.scn_height // 2 - TOLERANCE)
            car.goto(x=self.scn_width // 2 + TOLERANCE, y=y_cor)
            self.cars.append(car)

    def move_cars(self):
        for car in self.cars:
            speed = DIFFICULTY[car.color()[0]]
            car.goto(x=car.xcor() - speed, y=car.ycor())
