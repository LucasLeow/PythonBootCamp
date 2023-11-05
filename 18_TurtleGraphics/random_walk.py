from turtle import Turtle, Screen
import random

distance = 30

t = Turtle()
r = lambda: random.randint(0,255)
t.pensize(15)
t.speed(10)
direction = [0, 90, 180, 270]

while True:
    random_hex = '#%02X%02X%02X' % (r(), r(), r())
    t.color(random_hex)
    t.setheading(random.choice(direction))
    t.forward(distance)
