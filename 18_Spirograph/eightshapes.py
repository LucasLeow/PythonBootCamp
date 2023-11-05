from turtle import Turtle, Screen
import random

# Interior angle = (n-2)*180
sides = [3,4,5,6,7,8,9,10]
colors = []

r = lambda: random.randint(0,255)
t = Turtle()
t.shape('turtle')
length = 100

for side in sides:
    random_hex = '#%02X%02X%02X' % (r(), r(), r())
    t.color(random_hex)
    interior_angle = ((side - 2) * 180) / side
    for _ in range(side):
        t.forward(length)
        t.right(180 - interior_angle)

scn = Screen()
scn.exitonclick()







