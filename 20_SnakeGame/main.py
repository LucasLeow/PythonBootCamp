from snake import Snake
from turtle import Screen

# Setup Screen
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600
MOVE_DIST = 20

scn = Screen()
scn.setup(width=SCREEN_WIDTH, height=SCREEN_HEIGHT)
scn.bgcolor('black')
scn.title('Snake Game')
scn.tracer(n=0)  # n = 0 means turn off auto-update, call scn.update() at desired places

scn.listen()
scn.onkeypress(key="Up", fun=game.move_north)
scn.onkeypress(key="Down", fun=game.move_south)
scn.onkeypress(key="Left", fun=game.move_west)
scn.onkeypress(key="Right", fun=game.move_east)

game = Snake()
game.create_snake()

game_is_on = True
while game_is_on:
    scn.update()
    game.move_snake(MOVE_DIST)

scn.exitonclick()