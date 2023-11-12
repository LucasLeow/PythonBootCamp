from turtle import Turtle

FONT = ('Consolas', 18, 'normal')
GAMEOVR_FONT = ("sans-serif", 20, 'bold')
ALIGN = 'center'
TOLERANCE = 20 + FONT[1]

class Scoreboard(Turtle):
    def __init__(self, scn_width, scn_height):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.color('black')
        self.level = 1
        self.scn_width = scn_width
        self.scn_height = scn_height
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.goto(x=-(self.scn_width // 2) + TOLERANCE + FONT[1], y=self.scn_height // 2 - TOLERANCE)
        self.write(f"Level: {self.level}", align=ALIGN, font=FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write('GAME OVER', move=False, align=ALIGN, font=GAMEOVR_FONT)
