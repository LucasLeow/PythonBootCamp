from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import ScoreBoard
import time

# Constants
WIN_SCORE = 5
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

RIGHT_PADDLE_POS = 350
LEFT_PADDLE_POS = -350

WALL_TOLERANCE = 10
PADDLE_TOLERANCE = 20
DEFAULT_BOUNCE_DELAY = 0.08


bounce_delay = DEFAULT_BOUNCE_DELAY
bounce_step = 0.005

if __name__ == '__main__':
    scn = Screen()
    scn.setup(width=SCREEN_WIDTH, height=SCREEN_HEIGHT)
    scn.bgcolor('black')
    scn.title('Pong')
    scn.tracer(n=0)

    r_paddle = Paddle(RIGHT_PADDLE_POS, 0, SCREEN_HEIGHT)
    l_paddle = Paddle(LEFT_PADDLE_POS, 0, SCREEN_HEIGHT)
    score = ScoreBoard(SCREEN_HEIGHT)
    b = Ball()

    scn.listen()
    scn.onkeypress(key="Up", fun=r_paddle.move_paddle_up)
    scn.onkeypress(key="Down", fun=r_paddle.move_paddle_down)
    scn.onkeypress(key="w", fun=l_paddle.move_paddle_up)
    scn.onkeypress(key="s", fun=l_paddle.move_paddle_down)

    game_is_on = True
    while game_is_on:
        if score.r_score == WIN_SCORE:
            game_is_on = False
            score.show_winner('Right Paddle')
        if score.l_score == WIN_SCORE:
            game_is_on = False
            score.show_winner('Left Paddle')
        scn.update()
        b.move()
        # Detect collision with walls
        if (
            b.ycor() >= (SCREEN_HEIGHT // 2) - WALL_TOLERANCE or
            b.ycor() <= -(SCREEN_HEIGHT // 2) + WALL_TOLERANCE
        ):
            b.wall_bounce()

        # Detect collision with paddle
        if (
            b.distance(r_paddle) <= 50 and b.xcor() > RIGHT_PADDLE_POS - PADDLE_TOLERANCE or
            b.distance(l_paddle) <= 50 and b.xcor() < LEFT_PADDLE_POS + PADDLE_TOLERANCE
        ):
            b.paddle_bounce()
            if bounce_delay > 0.04:
                bounce_delay -= bounce_step
            if bounce_delay <= 0.04:
                bounce_step = 0.003
                bounce_delay -= bounce_step

        # Right paddle miss
        if (
            b.distance(r_paddle) > 50 and b.xcor() > RIGHT_PADDLE_POS + WALL_TOLERANCE
        ):
            b.reset_ball()
            bounce_delay = DEFAULT_BOUNCE_DELAY
            score.increment_left()
            score.update_scoreboard()
            scn.update()
            # Put timer here
            time.sleep(1)

        # Left paddle miss
        if (
            b.distance(l_paddle) > 50 and b.xcor() < LEFT_PADDLE_POS - WALL_TOLERANCE
        ):
            b.reset_ball()
            bounce_delay = DEFAULT_BOUNCE_DELAY
            score.increment_right()
            score.update_scoreboard()
            scn.update()
            # Put timer here
            time.sleep(0.5)

        time.sleep(bounce_delay)
        print(bounce_delay)


    scn.exitonclick()
