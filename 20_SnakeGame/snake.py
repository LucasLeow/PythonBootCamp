from turtle import Turtle, Screen
import time

class SnakeGame:
    def __init__(self):
        self.snake = []

    def create_snake(self):
        x_pos = 0
        y_pos = 0
        for _ in range(3):
            t = Turtle(shape="square")
            t.color('white')
            t.penup()
            t.goto(x_pos, y_pos)
            x_pos -= 20
            self.snake.append(t)


    def move_snake(self, dist):
        # self.scn.listen()
        #     self.scn.onkeypress(key="Left", fun=self.turn_left)
        #     self.scn.onkeypress(key="Right", fun=self.turn_right)
        #     self.scn.update() # move entire snake instead of by parts
        for i in range(len(self.snake) - 1, 0, -1):
            self.snake[i].goto(self.snake[i-1].position())
            time.sleep(0.1)
        self.snake[0].forward(dist)

    def turn_left(self):d
        cur_hdg = self.snake[0].heading()
        self.snake[0].setheading(cur_hdg + 90)

    def turn_right(self):
        cur_hdg = self.snake[0].heading()
        self.snake[0].setheading(cur_hdg - 90)

