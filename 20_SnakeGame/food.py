from turtle import Turtle
import random
class Food(Turtle):
    GAP = 20
    def __init__(self, scn_width, scn_height):
        super().__init__()
        self.scn_width = scn_width
        self.scn_height = scn_height
        self.shape('circle')
        self.color('blue')
        self.shapesize(stretch_len=0.5, stretch_wid=0.5) # 20 * 0.5 = 10 x 10 circle
        self.speed('fastest')
        self.penup()
        self.goto(
            x=random.randint(-int(scn_width/2) + Food.GAP, int(scn_width/2) - Food.GAP),
            y=random.randint(-int(scn_height/2) + Food.GAP, int(scn_height/2) - Food.GAP)
                  )

    def refresh(self):
        self.goto(
            x=random.randint(-int(self.scn_width / 2) + Food.GAP, int(self.scn_width / 2) - Food.GAP),
            y=random.randint(-int(self.scn_height / 2) + Food.GAP, int(self.scn_height / 2) - Food.GAP)
        )
