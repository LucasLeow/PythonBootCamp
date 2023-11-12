from turtle import Turtle

MOVEMENT_DIST = 20

class TurtlePiece(Turtle):
    def __init__(self, scn_height):
        super().__init__(shape='turtle')
        self.penup()
        self.setheading(90)
        self.speed('fastest')
        self.scn_height = scn_height
        self.goto(x=0, y=-scn_height//2+20)

    def move_forward(self):
        self.forward(MOVEMENT_DIST)

    def move_backward(self):
        if self.ycor() <= -self.scn_height//2+20:
            return
        self.backward(MOVEMENT_DIST)

