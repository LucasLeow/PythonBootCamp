from turtle import Turtle

class Paddle:
    def __init__(self):
        self.right_paddle = None
        self.left_paddle = None

    def create_part(self):
        scaler = 5 # 5 * 20 = 100
        p = Turtle(shape='square')
        p.color('white')
        p.shapesize(stretch_len=1, stretch_wid=scaler)
        p.penup()
        p.speed('fastest')
        return p

    def setup_paddles(self):
        right_x_pos = 350
        left_x_pos = -350
        y_pos = 0
        self.right_paddle = self.create_part()
        self.left_paddle = self.create_part()
        self.right_paddle.goto(right_x_pos, y_pos)
        self.left_paddle.goto(left_x_pos, y_pos)

    def right_paddle_up(self):
        self.right_paddle.sety(self.right_paddle.ycor() + 20)

    def right_paddle_down(self):
        self.right_paddle.sety(self.right_paddle.ycor() - 20)
