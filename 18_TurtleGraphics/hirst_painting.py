from turtle import Turtle, Screen
import random
import colorgram

DOT_SIZE = 20
MARCH_LENGTH = 50
X_START = -500
Y_START = -500

colors = colorgram.extract('spot_colors.jpg', 10)

def get_random_color(all_colors):
    random_color = random.choice(all_colors)
    return (random_color.rgb[0], random_color.rgb[1], random_color.rgb[2])

def draw_hirst(rows, cols):
    t = Turtle()
    scn = Screen()
    scn.colormode(255)
    t.speed('fastest')

    # Get to starting position
    t.penup()
    t.goto(X_START, Y_START)
    t.pendown()

    print(t.position())

    for i in range(rows):
        t.penup()
        t.goto(X_START, Y_START + (i * 40))
        t.pendown()
        for _ in range(cols):
            t.dot(DOT_SIZE, get_random_color(colors))
            t.penup()
            t.forward(MARCH_LENGTH)
            t.pendown()


    scn.exitonclick()

draw_hirst(10,10)


