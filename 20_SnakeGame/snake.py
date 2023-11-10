from turtle import Turtle, Screen
import time

class Snake:
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
        for i in range(len(self.snake) - 1, 0, -1):
            self.snake[i].speed('fastest')
            self.snake[i].goto(self.snake[i-1].position())
            time.sleep(0.05)
        self.snake[0].forward(dist)

    def move_north(self):
        if self.snake[0].heading() != 270:
            self.snake[0].setheading(90)

    def move_south(self):
        if self.snake[0].heading() != 90:
            self.snake[0].setheading(270)

    def move_east(self):
        if self.snake[0].heading() != 180:
            self.snake[0].setheading(0)

    def move_west(self):
        if self.snake[0].heading() != 0:
            self.snake[0].setheading(180)

