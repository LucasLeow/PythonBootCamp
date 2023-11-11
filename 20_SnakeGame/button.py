from turtle import Turtle

CURSOR_SIZE = 30
FONT_SIZE = 15

FONT = ('Arial', 18, 'bold')
class Button(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.shape('circle')
        self.shapesize(2, 2)
        self.penup()
        self.speed('fastest')

    def easy_button(self):
        self.goto(-170, -180)
        self.color('Limegreen')
        self.write("Easy Mode", align='center', font=FONT)
        self.sety(-180 + CURSOR_SIZE + FONT_SIZE)
        self.onclick(self.easy_clicked)
        self.showturtle()

    def easy_clicked(self,x ,y):
        return "easy"


