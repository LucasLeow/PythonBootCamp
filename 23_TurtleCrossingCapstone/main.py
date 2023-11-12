from turtle import Screen
from turtle_piece import TurtlePiece
from car_manager import CarManager
from scoreboard import Scoreboard

import time

# Constants
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600
TOLERANCE = 20
DEFAULT_TIMER = 0.1

if __name__ == '__main__':
    scn = Screen()
    scn.setup(width=SCREEN_WIDTH, height=SCREEN_HEIGHT)
    scn.title('Turtle Crossing')
    scn.tracer(n=0)

    t = TurtlePiece(SCREEN_HEIGHT)
    score = Scoreboard(SCREEN_WIDTH, SCREEN_HEIGHT)
    cm = CarManager(SCREEN_WIDTH, SCREEN_HEIGHT, score.level)

    scn.listen()
    scn.onkeypress(key="Up", fun=t.move_forward)
    scn.onkeypress(key="Down", fun=t.move_backward)

    game_is_on = True
    while game_is_on:
        cm.level = score.level
        time.sleep(DEFAULT_TIMER)  # Controls overall speed of game
        scn.update()

        cm.generate_car()
        cm.move_cars()

        # Detect collision
        for car in cm.cars:
            if t.distance(car) <= 23:
                game_is_on = False
                score.game_over()

        # Detect Turtle reach other side
        if t.ycor() >= SCREEN_HEIGHT // 2 - TOLERANCE:
            t.goto(x=0, y=-SCREEN_HEIGHT//2+20)
            score.level += 1
            score.update_scoreboard()
            if DEFAULT_TIMER > 0.08:
                DEFAULT_TIMER -= 0.005
            if DEFAULT_TIMER < 0.06:
                DEFAULT_TIMER -= 0.002
            if DEFAULT_TIMER < 0.04:
                DEFAULT_TIMER = 0.04






    scn.exitonclick()
