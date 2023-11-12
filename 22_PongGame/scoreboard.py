from turtle import Turtle

ALIGN = 'center'
FONT = ('Consolas', 18, 'normal')
GAMEOVR_FONT = ("sans-serif", 30, 'bold')
SCORE_FONT = ('Consolas', 40, 'normal')
TOP_GAP = SCORE_FONT[1] + 30

class ScoreBoard(Turtle):
    def __init__(self, scn_height):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.l_score = 0
        self.r_score = 0
        self.scn_height = scn_height
        self.color('white')
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.goto(-(SCORE_FONT[1] + 50), y=self.scn_height // 2 - TOP_GAP)
        self.write(self.l_score, align=ALIGN, font=SCORE_FONT)

        self.goto((SCORE_FONT[1] + 50), y=self.scn_height // 2 - TOP_GAP)
        self.write(self.r_score, align=ALIGN, font=SCORE_FONT)


    def increment_left(self):
        self.l_score += 1

    def increment_right(self):
        self.r_score += 1

    def show_winner(self, winner):
        self.goto(0, 0)
        game_ovr_txt = "GAME OVER"
        self.color('red')
        self.write(game_ovr_txt, move=False, align=ALIGN, font=GAMEOVR_FONT)
        self.goto(0, -20)
        self.color('white')
        self.write(f'The winner is {winner}', move=False, align=ALIGN, font=FONT)