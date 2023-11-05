from turtle import Turtle, Screen
import random

RADIUS = 100

t = Turtle()
t.speed(100)

r = lambda: random.randint(0,255)

def draw_spirograph(step):
    for i in range(0, 360, step):

        random_hex = '#%02X%02X%02X' % (r(), r(), r())
        t.color(random_hex)

        t.setheading(i)
        t.circle(RADIUS)

draw_spirograph(5)

scn = Screen()
scn.exitonclick()