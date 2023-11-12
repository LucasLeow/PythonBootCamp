from turtle import Turtle

class Paddle(Turtle):
    def __init__(self, xcor, ycor, SCN_HEIGHT):
        super().__init__(shape='square')
        self.color('white')
        self.shapesize(stretch_len=1, stretch_wid=5)
        self.penup()
        self.speed('fastest')
        self.goto(xcor, ycor)
        self.scn_height = SCN_HEIGHT


    def move_paddle_up(self):
        if self.ycor() <= self.scn_height // 2 - 65:
            self.sety(self.ycor() + 20)

    def move_paddle_down(self):
        if self.ycor() >= - self.scn_height // 2 + 65:
            self.sety(self.ycor() - 20)
