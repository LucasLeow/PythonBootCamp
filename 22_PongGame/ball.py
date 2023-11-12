from turtle import Turtle
import time

#Constants
BALL_MOVE_DIST = 10
new_x = 0
new_y = 0

class Ball(Turtle):
    def __init__(self):
        super().__init__(shape='circle')
        self.color('white')
        self.penup()
        self.x_move = 10
        self.y_move = 10

    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def wall_bounce(self):
        self.y_move *= -1

    def paddle_bounce(self):
        self.x_move *= -1

    def reset_ball(self):
        self.home()
        self.y_move *= -1
        self.x_move *= -1



