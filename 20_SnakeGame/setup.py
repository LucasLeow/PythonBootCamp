from turtle import Turtle
from art import logo
from button import Button
class Setup(Turtle):
    def __init__(self, screen_width, screen_height):
        super().__init__()
        self.hideturtle()
        self.penup()

        self.goto(x=-screen_width / 2 + screen_width / 5, y=0)
        self.color('white')
        self.speed('fastest')
        self.write(logo, move=False, font=('consolas', 8, 'normal'))

        self.goto(x=-screen_width / 2 + screen_width / 2.5, y=-50)
        self.write('Snake', move=False, font=('consolas', 30, 'normal'))

        self.goto(x=-screen_width / 2 + screen_width / 5, y=-100)
        self.write('Choose Difficulty', move=False, font=('consolas', 30, 'normal'))
