from turtle import Turtle, Screen
import time

class Snake:
    def __init__(self):
        self.snake = []

    def create_part(self):
        scaler = 1
        t = Turtle(shape="square")
        t.color('white')
        t.shapesize(stretch_len=scaler, stretch_wid=scaler)
        t.penup()
        t.speed('fastest')
        return t

    def create_snake(self):
        x_pos = 0
        y_pos = 0
        for _ in range(3):
            t = self.create_part()
            t.goto(x_pos, y_pos)
            x_pos -= 20
            self.snake.append(t)

    def lengthen_snake(self):
        self.snake.append(self.create_part())

    def move_snake(self, dist):
        for i in range(len(self.snake) - 1, 0, -1):
            self.snake[i].speed('fastest')
            self.snake[i].goto(self.snake[i-1].position())
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

    def reset_snake(self):
        for seg in self.snake:
            seg.reset()
        self.snake.clear()
        self.create_snake()

