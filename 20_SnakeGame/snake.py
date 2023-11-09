from turtle import Turtle, Screen

class SnakeGame:
    SCREEN_WIDTH=600
    SCREEN_HEIGHT=600
    def __init__(self):
        self.scn = Screen()
        self.snake = []

    def screen_setup(self):
        self.scn.setup(width=SnakeGame.SCREEN_WIDTH, height=SnakeGame.SCREEN_HEIGHT)
        self.scn.bgcolor('black')
        self.scn.title('Snake Game')

    def create_snake(self):
        for _ in range(3):
            t = Turtle(shape="square")
            t.color('white')
            self.snake.append(t)

    def start_snake(self):
        x_pos = 0
        y_pos = 0
        self.create_snake()
        for snake_part in self.snake:
            snake_part.penup()
            snake_part.speed(0)
            snake_part.goto(x_pos, y_pos)
            x_pos -= 20


if __name__ == '__main__':
    game = SnakeGame()
    game.screen_setup()
    game.start_snake()


    game.scn.exitonclick()