from turtle import Turtle

ALIGN = "center"
FONT = ('Consolas', 18, 'normal')
TOP_GAP = 30

class ScoreBoard(Turtle):
    def __init__(self, scn_height):
        super().__init__()
        self.score = 0
        self.hideturtle()
        self.penup()
        self.speed('fastest')
        self.goto(x=0, y=scn_height/2 - TOP_GAP)
        self.color('white')

    def display_score(self):
        text = f"Score: {self.score}"
        self.write(text, move=False, align=ALIGN, font=FONT)

    def increment_score(self):
        self.score += 1
        self.clear()
        self.display_score()