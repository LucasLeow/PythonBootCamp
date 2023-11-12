from turtle import Turtle

class Paddle(Turtle):
    def __init__(self, xcor, ycor):
        super().__init__(shape='square')
        self.color('white')
        self.shapesize(stretch_len=1, stretch_wid=5)
        self.penup()
        self.speed('fastest')
        self.goto(xcor, ycor)


    def move_paddle_up(self):
        self.sety(self.ycor() + 20)

    def move_paddle_down(self):
        self.sety(self.ycor() - 20)
