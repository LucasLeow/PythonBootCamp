from turtle import Turtle

class TurtlePiece(Turtle):
    def __init__(self, scn_height):
        super().__init__(shape='turtle')
        self.penup()
        self.setheading(90)
        self.speed('fastest')
        self.goto(x=0, y=-scn_height//2+20)

    def move(self):
        self.forward(10)

