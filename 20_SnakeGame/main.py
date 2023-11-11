# == Imports ==
from snake import Snake
from turtle import Screen
import time
from food import Food
from scoreboard import ScoreBoard

# == Constants ==
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600
MOVE_DIST = 20
FOOD_TOLERANCE = 15
TOP_AND_LEFT_TOLERANCE = 10
BOTTOM_AND_RIGHT_TOLERANCE = 20

# == Setup Screen ==
scn = Screen()
scn.setup(width=SCREEN_WIDTH, height=SCREEN_HEIGHT)
scn.bgcolor('black')
scn.title('Snake Game')
scn.tracer(n=0)  # n = 0 means turn off auto-update, call scn.update() at desired places

# == Game Setup ==
game = Snake()
game.create_snake()
food = Food(SCREEN_WIDTH, SCREEN_HEIGHT)
score = ScoreBoard(SCREEN_HEIGHT)

scn.listen()
scn.onkeypress(key="Up", fun=game.move_north)
scn.onkeypress(key="Down", fun=game.move_south)
scn.onkeypress(key="Left", fun=game.move_west)
scn.onkeypress(key="Right", fun=game.move_east)

# == Game Operation ==
game_is_on = True
while game_is_on:
    score.display_score()
    scn.update()
    if game.snake[0].distance(food) < FOOD_TOLERANCE:
        game.lengthen_snake()
        score.increment_score()
        food.refresh()

    if (
            (game.snake[0].xcor() >= (SCREEN_WIDTH // 2) - BOTTOM_AND_RIGHT_TOLERANCE) or
            (game.snake[0].xcor() <= -(SCREEN_WIDTH // 2) + TOP_AND_LEFT_TOLERANCE) or
            (game.snake[0].ycor() >= (SCREEN_HEIGHT // 2) - TOP_AND_LEFT_TOLERANCE) or
            (game.snake[0].ycor() <= -(SCREEN_HEIGHT // 2) + BOTTOM_AND_RIGHT_TOLERANCE)
    ):
        score.display_game_over()
        game_is_on = False

    time.sleep(0.1)
    game.move_snake(MOVE_DIST)


scn.exitonclick()