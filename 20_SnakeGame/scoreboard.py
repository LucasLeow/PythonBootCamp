from turtle import Turtle

ALIGN = "center"
FONT = ('Consolas', 18, 'normal')
GAMEOVR_FONT = ("sans-serif", 30, 'bold')
TOP_GAP = 30

with open('hi_score.txt', mode='r') as file:
    hi_score = int(file.read())

print(hi_score)
class ScoreBoard(Turtle):
    def __init__(self, scn_height):
        super().__init__()
        self.score = 0
        self.high_score = hi_score
        self.hideturtle()
        self.penup()
        self.speed('fastest')
        self.goto(x=0, y=scn_height/2 - TOP_GAP)
        self.color('white')

    def display_score(self):
        self.clear()
        text = f"Score: {self.score} Highscore: {self.high_score}"
        self.write(text, move=False, align=ALIGN, font=FONT)

    def reset_scoreboard(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open('hi_score.txt', mode='w') as file:
                file.write(str(self.high_score))

        self.score = 0

    # def display_game_over(self):
    #     self.goto(0, 0)
    #     game_ovr_txt = "GAME OVER"
    #     self.color('red')
    #     self.write(game_ovr_txt, move=False, align=ALIGN, font=GAMEOVR_FONT)
    #     self.goto(0, -20)
    #     self.color('white')
    #     self.write(f'Final Score: {self.score}', move=False, align=ALIGN, font=FONT)

    def increment_score(self):
        self.score += 1
        self.display_score()