from turtle import Turtle
import random
import time

# blue = slowest, indigo = fastest
COLORS = ['blue', 'green', 'yellow', 'orange', 'red', 'indigo']
DIFFICULTY = {
    'blue': 5,
    'green': 8,
    'yellow': 11,
    'orange': 15,
    'red': 18,
    "indigo": 20
}
START_MOVE_DIST = 5
MOVE_INCREMENT = 30
TOLERANCE = 35


class CarManager:
    def __init__(self, scn_width, scn_height):
        self.level = 1
        self.scn_width = scn_width
        self.scn_height = scn_height
        self.cars = []

    def generate_car(self):
        seed = random.randint(1, 6)
        if seed == 1:
            car = Turtle(shape='square')
            car.shapesize(stretch_len=2, stretch_wid=1)
            car.color(random.choice(list(DIFFICULTY.keys())))
            car.penup()
            car.speed('fastest')

            y_cor = random.randint(-self.scn_height//2 + TOLERANCE, self.scn_height//2 - TOLERANCE)
            car.goto(x=self.scn_width//2 + TOLERANCE, y=y_cor)
            self.cars.append(car)

    def move_cars(self):
        for car in self.cars:
            speed = DIFFICULTY[car.color()[0]]
            car.goto(x=car.xcor() - speed, y=car.ycor())





