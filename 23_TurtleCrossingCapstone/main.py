from turtle import Screen
from turtle_piece import TurtlePiece
from car_manager import CarManager

import time

# Constants
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600

if __name__ == '__main__':
    scn = Screen()
    scn.setup(width=SCREEN_WIDTH, height=SCREEN_HEIGHT)
    scn.title('Turtle Crossing')
    scn.tracer(n=0)

    t = TurtlePiece(SCREEN_HEIGHT)
    cm = CarManager(SCREEN_WIDTH, SCREEN_HEIGHT)

    scn.listen()
    scn.onkeypress(key="Up", fun=t.move)

    game_is_on = True
    while game_is_on:
        cm.generate_car()
        cm.move_cars()
        scn.update()
        time.sleep(0.1) # Controls overall speed of game

    scn.exitonclick()
