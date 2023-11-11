# == Imports ==
from snake import Snake
from turtle import Screen, Turtle
from food import Food
from scoreboard import ScoreBoard
from setup import Setup

import time

# == Constants ==
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600
MOVE_DIST = 20
FOOD_TOLERANCE = 15
TOP_AND_LEFT_TOLERANCE = 5
BOTTOM_AND_RIGHT_TOLERANCE = 15
CURSOR_SIZE = 20
FONT_SIZE = 15
FONT = ('Arial', FONT_SIZE, 'normal')


def snake_game_start(x, y):
    if x <= -110:
        timer = 0.1
    elif x> -110 and x < 20:
        timer = 0.075
    elif x >= 20:
        timer = 0.05

    scn.reset()
    scn.tracer(n=0)  # n = 0 means turn off auto-update, call scn.update() at desired places

    # == Game Setup ==
    game = Snake()
    game.create_snake()
    food = Food(SCREEN_WIDTH, SCREEN_HEIGHT)
    score = ScoreBoard(SCREEN_HEIGHT)
    scn.update()

    scn.listen()
    scn.onkeypress(key="Up", fun=game.move_north)
    scn.onkeypress(key="Down", fun=game.move_south)
    scn.onkeypress(key="Left", fun=game.move_west)
    scn.onkeypress(key="Right", fun=game.move_east)

    # Game Operation ==
    game_is_on = True
    while game_is_on:
        score.display_score()
        scn.update()
        if game.snake[0].distance(food) < FOOD_TOLERANCE:
            game.lengthen_snake()
            score.increment_score()
            food.refresh()

        # Detect collision at border
        if (
                (game.snake[0].xcor() >= (SCREEN_WIDTH // 2) - BOTTOM_AND_RIGHT_TOLERANCE) or
                (game.snake[0].xcor() <= -(SCREEN_WIDTH // 2) + TOP_AND_LEFT_TOLERANCE) or
                (game.snake[0].ycor() >= (SCREEN_HEIGHT // 2) - TOP_AND_LEFT_TOLERANCE) or
                (game.snake[0].ycor() <= -(SCREEN_HEIGHT // 2) + BOTTOM_AND_RIGHT_TOLERANCE)
        ):
            score.display_game_over()
            game_is_on = False

        # Detect collision with tail
        for i in range(1, len(game.snake)):
            if game.snake[0].distance(game.snake[i]) < 10:
                score.display_game_over()
                game_is_on = False

        time.sleep(timer)
        game.move_snake(MOVE_DIST)


def easy_button():
    button = Turtle()
    button.hideturtle()
    button.shape('circle')

    button.penup()
    button.goto(-150, -180)
    button.color('Limegreen')
    button.write("Easy Mode", align='center', font=FONT)
    button.sety(-180 + CURSOR_SIZE + FONT_SIZE)
    button.onclick(snake_game_start)
    button.showturtle()

def medium_button():
    button = Turtle()
    button.hideturtle()
    button.shape('circle')

    button.penup()
    button.goto(0, -180)
    button.color('orange')
    button.write("Medium Mode", align='center', font=FONT)
    button.sety(-180 + CURSOR_SIZE + FONT_SIZE)
    button.onclick(snake_game_start)
    button.showturtle()

def hard_button():
    button = Turtle()
    button.hideturtle()
    button.shape('circle')

    button.penup()
    button.goto(150, -180)
    button.color('red')
    button.write("Hard Mode", align='center', font=FONT)
    button.sety(-180 + CURSOR_SIZE + FONT_SIZE)
    button.onclick(snake_game_start)
    button.showturtle()


if __name__ == '__main__':
    # == Setup Screen ==
    scn = Screen()

    scn.setup(width=SCREEN_WIDTH, height=SCREEN_HEIGHT)
    scn.bgcolor('black')
    scn.title('Snake Game')
    scn.tracer(n=0)

    game_setup = Setup(SCREEN_WIDTH, SCREEN_HEIGHT)
    easy_button()
    medium_button()
    hard_button()
    scn.update()
    scn.mainloop()

